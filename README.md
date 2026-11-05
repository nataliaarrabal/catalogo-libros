# 📚 Catálogo de libros con recomendaciones

> TODO (Semana 4): reescribe esta intro con tus palabras: qué hace, captura del terminal y qué has aprendido.

Aplicación de terminal en Python + MySQL para gestionar tu biblioteca personal y recibir recomendaciones, construida sobre el dataset público [goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k) (10.000 libros).

## Tecnologías

Python 3.10+ · MySQL 8 · Typer · pytest · Docker (para la base de datos)

## Puesta en marcha

### 1. Base de datos MySQL

**Opción A, con Docker (recomendada):**
```bash
cp .env.example .env        # en Windows: copy .env.example .env
# edita .env y pon tus contraseñas
docker compose up -d
```

**Opción B, MySQL instalado en tu equipo:** crea la base de datos y el usuario:
```sql
CREATE DATABASE libros CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE USER 'libros'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON libros.* TO 'libros'@'localhost';
```
y pon esos datos en `.env`.

### 2. Entorno de Python
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -e ".[dev]"
```

### 3. Datos y tablas
```bash
python -m libros.download     # descarga los CSV en data/
python -m libros.create_db    # crea las tablas
python -m libros.etl          # importa los datos
```

### 4. ¡A usarla!
```bash
libros --help
libros buscar "harry potter"
libros añadir 2 --estado leido --nota 5
libros recomendar
```

### Tests
```bash
pytest -v
```

## Estructura

```
sql/schema.sql         Esquema de la base de datos
src/libros/db.py       Conexión a MySQL
src/libros/create_db.py  Crea las tablas
src/libros/download.py Descarga el dataset
src/libros/etl.py      Limpieza e importación de datos
src/libros/recommend.py  Lógica de recomendación
src/libros/cli.py      Comandos de terminal
tests/                 Tests con pytest
```

## Hoja de ruta · Fase 1

- [ ] **Semana 1:** repo en GitHub, MySQL funcionando, tablas `tags`, `book_tags` y `my_library` en `schema.sql`
- [ ] **Semana 2:** `parse_year`, `parse_isbn`, `parse_authors` (¡tests en verde!), `import_authors`, `import_tags`
- [ ] **Semana 3:** comandos `añadir`, `mi-biblioteca`, `recomendar`; búsqueda por autor
- [ ] **Semana 4:** comando `estadisticas`, tests propios, README final con capturas

## Decisiones de diseño

> TODO: ve anotando aquí tus decisiones y el porqué. A los entrevistadores les encanta esta sección.
> Ejemplos: ¿por qué MySQL? ¿qué etiquetas filtraste y por qué? ¿cómo puntúas las recomendaciones?

## Próximas fases

2. API REST con FastAPI · 3. Frontend con React + TypeScript · 4. Recomendaciones con filtrado colaborativo · 5. Docker, CI/CD y despliegue
