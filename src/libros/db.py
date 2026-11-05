"""Conexión a MySQL. Lee la configuración del archivo .env."""

import os
from contextlib import contextmanager

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "libros"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "libros"),
        charset="utf8mb4",
        collation="utf8mb4_0900_ai_ci",
    )


@contextmanager
def get_cursor(dictionary: bool = True):
    """Abre conexión + cursor; hace commit si todo va bien y rollback si falla.

    Uso:
        with get_cursor() as cur:
            cur.execute("SELECT COUNT(*) AS n FROM books")
            print(cur.fetchone()["n"])
    """
    conn = get_connection()
    cur = conn.cursor(dictionary=dictionary)
    try:
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
