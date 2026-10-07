
-- 1
INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date)
VALUES (11, 'Victor', 'Sago', 'vic.s@example.com', 'Stockholm', '2026-10-07');

-- 2
INSERT INTO products (name, category, price, stock)
VALUES
    ('Scarf', 'Accessories', 229, 15),
    ('Gloves', 'Accessories', 199, 20);

-- 3
INSERT INTO orders (order_id, customer_id, order_date)
VALUES (16, 7, '2026-10-07');   -- status defaults to 'new'

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);

-- 4
--INSERT INTO order_items (order_id, product_id, quantity, unit_price)
--VALUES (16, 1, 0, 100);
/* We get error:
CHECK constraint failed: quantity > 0 */

-- 5
UPDATE orders 
SET status = 'shipped'
WHERE order_id = 12;

-- 6
UPDATE products
SET stock = 50
WHERE product_id = 5;

-- 7
UPDATE products
SET price = ROUND(price * 1.1, 2)
WHERE category = 'Accessories';

-- 8
-- First to find the information:
SELECT order_id FROM orders
WHERE status = 'cancelled';
SELECT * FROM order_items
WHERE order_id IN (
	SELECT order_id FROM orders
	WHERE status = 'cancelled'
    );
-- Now to delete it
DELETE FROM order_items
WHERE order_id IN (
    SELECT order_id FROM orders 
    WHERE status = 'cancelled'
    );
DELETE FROM orders WHERE status = 'cancelled';
/* order_items.order_id is a foreign key to orders. Deleting the order first fails with FOREIGN KEY constraint failed, because the items would be left pointing at a missing order. */

-- 9
SELECT COUNT(*) FROM orders;

-- 10
-- phone_numbers holds several values in one cell, which breaks 1NF.
-- course1..3 is a repeating group:
--      at most 3 courses per student, many NULLs, finding who takes a course means searching 3 columns
-- If the student column holds a student's name, there's a risk of misspellings
-- There is no primary key, so two students with the same name can't be told apart.
-- Course names are free text, so typos and duplicates creep in.

-- 11
-- First of all, the table lacks a primary key. Without a PK we can' assess 
-- whether it breaks 2NF and 3NF.
-- It definitely breaks the 1NF -- cells in the `products` column hold 
-- multiple values, and also the amount.
-- If we assume that `order_no` serves as the PK, then it breaks 3NF, because
-- `email` and `city` don't depend on the `customer` and not on `order_no`.
-- (I presumed here that `city` is the customer's city.)
-- Lastly, the last column - `total` - is a derived value, and so shouldn't be 
-- stored but should rather be calculated from the price and amount.
-- To fix this, a new `order_items` table needs to be created, that holds a 
-- reference to the order (`order_sheet`), and another reference to a separate 
-- `products` table. It can also hold a value for `amount`.
-- Ideally, we should also have a `customers` table to hold a customer's name, 
-- email, and city, and use only `customer_id` to refer to the customer from 
-- the `order_sheet` table.

-- 12
-- If the PK in that table is only `order_id`, then `customer_email` breaks 3NF,
-- since it depends on `customer_id` and not on `order_id`. The same email 
-- would be repeated on every order and could become inconsistent.

-- 13
-- Candidates for entities are: students, teachers, lessons, instruments.
-- And probably rooms, too, although we can't conclude so with certainty 
-- from the description.

-- 14
/*
teacher - lesson        1:N
room - lesson           1:N
instrument - lesson     1:N
student - lesson	    1:M
teacher - instrument    N:M
*/
