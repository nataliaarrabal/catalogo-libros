"""Descarga los CSV de goodbooks-10k en la carpeta data/.

Uso:  python -m libros.download
"""

import urllib.request
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/"
FILES = ["books.csv", "tags.csv", "book_tags.csv"]  # ratings.csv (~70 MB) lo usaremos en la Fase 4
DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    for name in FILES:
        dest = DATA_DIR / name
        if dest.exists():
            print(f"Ya existe: {name}")
            continue
        print(f"Descargando {name}...")
        urllib.request.urlretrieve(BASE_URL + name, dest)
    print("Listo.")


if __name__ == "__main__":
    main()
