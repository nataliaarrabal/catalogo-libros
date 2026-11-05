"""Tests de las funciones de limpieza.

Al principio FALLAN (NotImplementedError): es a propósito.
Implementa las funciones en src/libros/etl.py hasta que pasen todos.
Ejecuta:  pytest -v
"""

from libros.create_db import split_statements
from libros.etl import parse_authors, parse_isbn, parse_year


# --- parse_year -------------------------------------------------------

def test_parse_year_normal():
    assert parse_year("1997.0") == 1997


def test_parse_year_negativo():
    assert parse_year("-720.0") == -720


def test_parse_year_vacio():
    assert parse_year("") is None


# --- parse_isbn -------------------------------------------------------

def test_parse_isbn_recupera_ceros():
    assert parse_isbn("439023483") == "0439023483"


def test_parse_isbn_vacio():
    assert parse_isbn("") is None


# --- parse_authors ----------------------------------------------------

def test_parse_authors_varios():
    assert parse_authors("J.K. Rowling, Mary GrandPré") == ["J.K. Rowling", "Mary GrandPré"]


def test_parse_authors_limpia_espacios_y_vacios():
    assert parse_authors("  Stephen King ,, ") == ["Stephen King"]


def test_parse_authors_sin_duplicados():
    assert parse_authors("Neil Gaiman, Terry Pratchett, Neil Gaiman") == [
        "Neil Gaiman",
        "Terry Pratchett",
    ]


# --- create_db (ya implementado: este test pasa desde el principio) ----

def test_split_statements_ignora_comentarios():
    sql = "-- comentario\nCREATE TABLE a (id INT);\n\nDROP TABLE b;\n"
    assert split_statements(sql) == ["CREATE TABLE a (id INT)", "DROP TABLE b"]


# TODO (Semana 4): añade tus propios tests, por ejemplo para la recomendación.
