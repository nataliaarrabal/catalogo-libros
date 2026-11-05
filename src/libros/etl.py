"""ETL: lee los CSV de goodbooks-10k, limpia los datos y los carga en MySQL.

Uso:  python -m libros.etl
(Antes: descargar los CSV con `python -m libros.download` y crear las tablas.)
"""

import csv
from pathlib import Path

from libros.db import get_cursor

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


# ------------------------------------------------------------------
# Funciones de limpieza (tienen tests en tests/test_etl.py)
# ------------------------------------------------------------------

def parse_year(raw: str) -> int | None:
    """Convierte el año del CSV en entero.

    '1997.0' -> 1997   |   '-720.0' -> -720   |   '' -> None
    """
    # TODO (Semana 2)
    raise NotImplementedError


def parse_isbn(raw: str) -> str | None:
    """El CSV perdió los ceros a la izquierda del ISBN-10.

    '439023483' -> '0439023483'   |   '' -> None
    Pista: str.zfill()
    """
    # TODO (Semana 2)
    raise NotImplementedError


def parse_authors(raw: str) -> list[str]:
    """Separa la cadena de autores en una lista limpia.

    'J.K. Rowling, Mary GrandPré' -> ['J.K. Rowling', 'Mary GrandPré']
    - Quita espacios sobrantes
    - Descarta vacíos
    - Elimina duplicados manteniendo el orden original
    """
    # TODO (Semana 2)
    raise NotImplementedError


# ------------------------------------------------------------------
# Carga en la base de datos
# ------------------------------------------------------------------

def read_csv(name: str) -> list[dict]:
    with open(DATA_DIR / name, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def import_books(cur, rows: list[dict]) -> int:
    """Ejemplo completo: inserta los libros. Úsalo de modelo para el resto."""
    values = [
        (
            int(r["book_id"]),
            int(r["goodreads_book_id"]),
            r["title"],
            r["original_title"] or None,
            parse_year(r["original_publication_year"]),
            parse_isbn(r["isbn"]),
            r["language_code"] or None,
            float(r["average_rating"]),
            int(r["ratings_count"]),
            r["image_url"],
        )
        for r in rows
    ]
    cur.executemany(
        """
        INSERT INTO books (id, goodreads_id, title, original_title, publication_year,
                           isbn, language_code, average_rating, ratings_count, image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        values,
    )
    return len(values)


def import_authors(cur, rows: list[dict]) -> int:
    """Inserta autores y la relación book_authors. Devuelve nº de autores.

    TODO (Semana 2). Pasos sugeridos:
      1. Recorre los libros y usa parse_authors() para obtener todos los nombres.
      2. Inserta los autores únicos en `authors` (executemany).
      3. Recupera sus ids:  SELECT id, name FROM authors  -> dict {name: id}
      4. Inserta en `book_authors` (book_id, author_id, position).
    """
    raise NotImplementedError


def import_tags(cur) -> int:
    """Carga tags.csv y book_tags.csv.

    TODO (Semana 2). Cuidado con dos trampas del dataset:
      - book_tags.csv usa `goodreads_book_id`, NO `book_id`.
        Necesitas traducirlo con la columna books.goodreads_id.
      - Hay etiquetas basura (p. ej. '-', 'to-read', 'favorites').
        Decide si filtrarlas y explica tu decisión en el README.
    """
    raise NotImplementedError


def main() -> None:
    books = read_csv("books.csv")
    with get_cursor() as cur:
        print(f"Libros:   {import_books(cur, books)}")
        print(f"Autores:  {import_authors(cur, books)}")
        print(f"Etiquetas:{import_tags(cur)}")


if __name__ == "__main__":
    main()
