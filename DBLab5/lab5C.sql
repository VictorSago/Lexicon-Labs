
-- 1
SELECT * FROM products
WHERE category IN ('Clothing', 'Accessories')
    AND price BETWEEN 150 AND 500
ORDER BY price DESC;


-- 2
SELECT * FROM orders
WHERE order_date LIKE '2026-02%' AND status <> 'cancelled';


-- 3
SELECT oi.order_id, p.name AS product_name, oi.quantity, 
        oi.quantity * oi.unit_price AS line_total
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
WHERE oi.quantity * oi.unit_price > 500
ORDER BY line_total DESC;


-- 4
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, c.city
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city IN ('Stockholm', 'Uppsala')


-- 5
-- The easiest solution would be using manual IDs. But we'll try to use the 
-- automatic IDs for both customer and order, and a lookup for product_id's.

-- Step 1: Insert the new customer
INSERT INTO customers (first_name, last_name, email, city, joined_date)
VALUES ('Leo', 'Falk', 'leo.falk@example.com', 'Uppsala', date('now'));

-- Steå 2: Insert the new order looking up customer's ID
INSERT INTO orders (customer_id, order_date)
SELECT customer_id, date('now')
FROM customers
WHERE email = 'leo.falk@example.com';

-- Step 3: Fill in order_items, looking up correct IDs from existing tables
-- and previous insertions. This works because 'Leo' is a new customer and
-- has no previous orders. If we had been dealing with an existing customer
-- we'd have to filter both by email and date in the `WHERE` clause.
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT o.order_id, p.product_id, v.quantity, p.price
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
CROSS JOIN (SELECT 'Hoodie Black' AS name, 1 AS quantity
            UNION ALL
            SELECT 'Socks 3-pack', 2) v
JOIN products p ON p.name = v.name
WHERE c.email = 'leo.falk@example.com';

-- Step 4: write out the receipt
SELECT p.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price AS line_total
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN customers c ON c.customer_id = o.customer_id
JOIN products p ON p.product_id = oi.product_id
WHERE c.email = 'leo.falk@example.com'
UNION ALL
SELECT 'Total', "...", "...", SUM(oi.quantity * oi.unit_price)
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN customers c ON c.customer_id = o.customer_id
WHERE c.email = 'leo.falk@example.com';
