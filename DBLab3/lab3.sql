
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
