
-- 1
SELECT o.order_id, c.first_name, c.last_name, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- 2
SELECT c.first_name, c.last_name, o.order_id, o.order_date, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Erik';

-- 3
SELECT c.first_name, c.last_name, o.order_id, o.order_date, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;

-- 4
SELECT oi.order_id, p.name, p.category, oi.quantity, oi.unit_price
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

-- 5
SELECT oi.order_id, p.name
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
WHERE p.category = 'Shoes';

-- 6
SELECT p.name, oi.quantity, oi.unit_price, 
    oi.unit_price * oi.quantity as line_total
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 10;

-- 7
SELECT c.first_name, o.order_date 
FROM customers c 
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p on oi.product_id = p.product_id
WHERE p.name = 'Hoodie Black';

-- 8
SELECT c.first_name, c.last_name, c.email, c.city, c.joined_date,
    o.order_id, o.order_date, o.status
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;

-- 9
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL;

-- 10
SELECT c.first_name, p.name, oi.quantity
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE c.city = 'Uppsala';
