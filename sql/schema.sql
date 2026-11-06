-- =============================================================
-- Catálogo de libros · Esquema MySQL 8
-- Ejecutar con: python -m libros.create_db
-- OJO: borra y recrea todas las tablas (se pierden los datos)
-- =============================================================

DROP TABLE IF EXISTS my_library;
DROP TABLE IF EXISTS book_tags;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS book_authors;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

-- -------------------------------------------------------------
-- Libros (una fila por libro de goodbooks-10k)
-- -------------------------------------------------------------
CREATE TABLE books (
    id               INT          PRIMARY KEY,          -- book_id del dataset (1..10000)
    goodreads_id     INT          NOT NULL UNIQUE,      -- goodreads_book_id (lo usa book_tags.csv)
    title            VARCHAR(500) NOT NULL,
    original_title   VARCHAR(500),
    publication_year SMALLINT,                          -- puede ser negativo (la Ilíada)
    isbn             CHAR(10),
    language_code    VARCHAR(10),
    average_rating   DECIMAL(3,2),
    ratings_count    INT,
    image_url        VARCHAR(500),
    FULLTEXT INDEX ft_books_title (title)               -- búsquedas rápidas por texto
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- -------------------------------------------------------------
-- Autores y relación muchos a muchos con libros
-- -------------------------------------------------------------
CREATE TABLE authors (
    id   INT          AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE book_authors (
    book_id   INT     NOT NULL,
    author_id INT     NOT NULL,
    position  TINYINT NOT NULL DEFAULT 1,   -- 1 = autor principal, 2 = segundo...
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id)   REFERENCES books(id)   ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE tags (
    id   INT     NOT NULL PRIMARY KEY,
    name VARCHAR(255)     NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE book_tags (
    book_id   INT     NOT NULL,
    tag_id INT     NOT NULL,
    tag_count INT NOT NULL, 
    PRIMARY KEY (book_id, tag_id),
    FOREIGN KEY (book_id)   REFERENCES books(id)   ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE my_library (
    book_id   INT     NOT NULL,
    status ENUM('quiero_leer','leyendo','leido')  NOT NULL,
    rating  TINYINT  CHECK (rating BETWEEN 1 AND 5),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    finished_at DATE,
    PRIMARY KEY (book_id),
    FOREIGN KEY (book_id)   REFERENCES books(id)   ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;