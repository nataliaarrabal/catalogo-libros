"""Crea (o recrea) las tablas ejecutando sql/schema.sql.

Uso:  python -m libros.create_db
"""

from pathlib import Path

from libros.db import get_cursor

SCHEMA_PATH = Path(__file__).resolve().parents[2] / "sql" / "schema.sql"


def split_statements(sql: str) -> list[str]:
    """Quita comentarios `--` y separa el script en sentencias por ';'."""
    lines = [line for line in sql.splitlines() if not line.strip().startswith("--")]
    clean = "\n".join(lines)
    return [stmt.strip() for stmt in clean.split(";") if stmt.strip()]


def main() -> None:
    statements = split_statements(SCHEMA_PATH.read_text(encoding="utf-8"))
    with get_cursor() as cur:
        for stmt in statements:
            cur.execute(stmt)
    print(f"Esquema creado: {len(statements)} sentencias ejecutadas.")


if __name__ == "__main__":
    main()
