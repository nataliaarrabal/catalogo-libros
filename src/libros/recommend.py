"""Recomendaciones. Fase 1: basadas en contenido (autores y etiquetas)."""


def recomendar_por_contenido(cur, limite: int = 10) -> list[dict]:
    """Recomienda libros parecidos a los que has valorado con 4 o más.

    TODO (Semana 3). Idea de enfoque con SQL:
      1. Tus libros favoritos:  my_library con rating >= 4
      2. Sus autores y sus etiquetas principales (book_tags con más `count`)
      3. Otros libros que compartan autor o etiqueta y que NO estén en my_library
      4. Puntúa cada candidato (p. ej. +3 por autor común, +1 por etiqueta común),
         desempata por average_rating y devuelve los `limite` mejores.

    Reto extra: explica en el README por qué elegiste esos pesos.
    """
    raise NotImplementedError
