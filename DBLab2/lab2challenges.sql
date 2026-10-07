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

-- 10
CREATE TABLE product_sizes (
    product_size_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    size TEXT NOT NULL CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER DEFAULT 0,
    UNIQUE (product_id, size),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
-- The first insertion works
INSERT INTO product_sizes (product_id, size) VALUES (1, 'M');
-- The second fails with 
/* UNIQUE constraint failed: product_sizes.product_id, product_sizes.size */
--INSERT INTO product_sizes (product_id, size) VALUES (1, 'M');

-- 11
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
INSERT INTO employees (first_name, last_name, manager_id) 
VALUES ('Boss', 'Bossman', NULL);

INSERT INTO employees (first_name, last_name, manager_id) 
VALUES 
    ('Alice', 'Enigma', 1), 
    ('Bob', 'Cypher', 1);

-- 12
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL UNIQUE
);
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT NOT NULL UNIQUE,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);
INSERT INTO teams (team_name) 
VALUES ('Tigers');
INSERT INTO players (player_name, team_id) 
VALUES 
    ('Charlie', 1), 
    ('Diana', 1);

DELETE FROM teams WHERE team_id = 1;
SELECT * FROM players;   -- 0 rows
