"""Interfaz de línea de comandos.

Uso:  libros --help
"""

from enum import Enum

import typer

from libros.db import get_cursor

app = typer.Typer(help="Catálogo de libros con recomendaciones.", no_args_is_help=True)


class Estado(str, Enum):
    quiero_leer = "quiero_leer"
    leyendo = "leyendo"
    leido = "leido"


@app.command()
def buscar(texto: str, limite: int = typer.Option(10, help="Máximo de resultados")):
    """Busca libros por título."""
    # Ejemplo completo. TODO (Semana 3): busca también por nombre de autor (JOIN).
    # Reto: prueba MATCH(title) AGAINST(%s) usando el índice FULLTEXT.
    with get_cursor() as cur:
        cur.execute(
            """
            SELECT id, title, publication_year, average_rating
            FROM books
            WHERE title LIKE %s
            ORDER BY ratings_count DESC
            LIMIT %s
            """,
            (f"%{texto}%", limite),
        )
        resultados = cur.fetchall()

    if not resultados:
        typer.echo("No se encontraron libros.")
        return
    for b in resultados:
        year = b["publication_year"] or "?"
        typer.echo(f"[{b['id']:>5}] {b['title']} ({year}) ★ {b['average_rating']}")


@app.command()
def añadir(
    book_id: int,
    estado: Estado = typer.Option(Estado.quiero_leer, help="Estado de lectura"),
    nota: int | None = typer.Option(None, min=1, max=5, help="Tu nota del 1 al 5"),
):
    """Añade un libro a tu biblioteca (o actualiza su estado y nota)."""
    # TODO (Semana 3): INSERT ... ON DUPLICATE KEY UPDATE en my_library.
    # Comprueba antes que el libro existe y muestra un mensaje claro si no.
    raise NotImplementedError


@app.command()
def mi_biblioteca(estado: Estado | None = typer.Option(None, help="Filtrar por estado")):
    """Lista los libros de tu biblioteca."""
    # TODO (Semana 3)
    raise NotImplementedError


@app.command()
def recomendar(limite: int = 10):
    """Recomienda libros según lo que te ha gustado."""
    # TODO (Semana 3): usa recommend.recomendar_por_contenido()
    raise NotImplementedError


@app.command()
def estadisticas():
    """Muestra estadísticas de tu biblioteca."""
    # TODO (Semana 4): autores más leídos, nota media, libros por estado,
    # mejores libros por etiqueta... ¡aquí luces tu SQL!
    raise NotImplementedError


if __name__ == "__main__":
    app()
