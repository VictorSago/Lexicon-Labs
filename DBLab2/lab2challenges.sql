-- 1
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT DEFAULT 'Sweden',
    email TEXT
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
    code TEXT PRIMARY KEY,
    discount_percent INTEGER NOT NULL CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);

--INSERT INTO coupons VALUES ('BIG95', 95, '2026-12-31');
/* We get error:
CHECK constraint failed: discount_percent BETWEEN 1 AND 90 */

-- 5
INSERT INTO suppliers (name) VALUES ('Baltic Wool');
SELECT * FROM suppliers;
-- gets id 2: INTEGER PRIMARY KEY fills itself with max(id) + 1

-- 6
ALTER TABLE suppliers 
RENAME COLUMN email TO contact_email;

-- 7
PRAGMA table_info(products);

-- 8
CREATE TABLE product_suppliers (
    product_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    purchase_price REAL NOT NULL CHECK (purchase_price > 0),
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO product_suppliers VALUES (1, 99, 100);
/* We get error:
FOREIGN KEY constraint failed */

-- 9
CREATE TABLE campaigns (
    campaign_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    CHECK (end_date >= start_date)
);

--INSERT INTO campaigns (name, start_date, end_date)
--VALUES ('Bad', '2026-06-10', '2026-06-01');
/* We get error:
CHECK constraint failed: end_date >= start_date */
