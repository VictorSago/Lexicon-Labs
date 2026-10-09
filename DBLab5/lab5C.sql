
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

