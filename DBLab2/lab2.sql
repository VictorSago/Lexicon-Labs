
-- 1
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER
);

--2
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER CHECK (publication_year > 1400)
);

--3
ALTER TABLE books
ADD COLUMN isbn TEXT;

--4
DROP TABLE IF EXISTS books;

--5
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--6
-- This setting causes SQLite to enforce the foreign keys constrain
/* If we're using DB Browser we don't need it, but if we're running
some other program we might need it. */ 
PRAGMA foreign_keys = ON;
-- INSERT INTO reviews (product_id, rating, comment)
-- VALUES (1, 6, 'Too good');
/* We get an error saying:
"CHECK constraint failed: rating BETWEEN 1 AND 5" */

--7
-- INSERT INTO reviews (product_id, rating, comment)
-- VALUES (50, 4, 'Ghost');
/* We get an error:
"Result: FOREIGN KEY constraint failed"
*/
