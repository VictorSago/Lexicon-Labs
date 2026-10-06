-- 1
CREATE TABLE suppliers (
  supplier_id INTEGER PRIMARY KEY,
  name        TEXT NOT NULL UNIQUE,
  country     TEXT DEFAULT 'Sweden',
  email       TEXT
);

-- 2
INSERT INTO suppliers (name) VALUES ('Nordic Textiles');

SELECT * FROM suppliers;
-- country = Sweden (the DEFAULT)

-- 3
--INSERT INTO suppliers (name) VALUES ('Nordic Textiles');
/* We get error:
UNIQUE constraint failed: suppliers.name */

-- 4
CREATE TABLE coupons (
  code             TEXT PRIMARY KEY,
  discount_percent INTEGER NOT NULL CHECK (discount_percent BETWEEN 1 AND 90),
  valid_until      TEXT NOT NULL
);

INSERT INTO coupons VALUES ('BIG95', 95, '2026-12-31');
/* We get error:
CHECK constraint failed: discount_percent BETWEEN 1 AND 90 */
