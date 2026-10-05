-- 1
SELECT first_name, last_name
FROM customers;

-- 2
SELECT *
FROM products
WHERE category = 'Shoes';

-- 3
SELECT *
FROM customers
WHERE city = 'Uppsala';

-- 4
SELECT *
FROM products
WHERE price = 199;

-- 5
SELECT *
FROM products
ORDER BY name;

-- 6
SELECT *
FROM customers
ORDER BY joined_date;

-- 7
SELECT *
FROM products
WHERE stock = 0;

-- 8
SELECT *
FROM customers
ORDER BY joined_date DESC
LIMIT 3;

-- 9
SELECT *
FROM customers
WHERE city IN ('Stockholm', 'Göteborg');

-- 10
SELECT name AS product, price AS price_sek
FROM products;

-- Bonus questions

-- 1
SELECT *
FROM products
WHERE category IN ('Shoes', 'Clothing') AND price > 1000;

SELECT *
FROM products
WHERE category = 'Shoes' OR category = 'Clothing' AND price > 1000;
/* Result is different because AND has a higher priority than OR */

-- 2
SELECT name, price, stock, price * stock AS stock_value
FROM products
ORDER by stock_value DESC;

-- 3
SELECT *
FROM customers
WHERE first_name LIKE '____';

/* This also works*/
SELECT *
FROM customers
WHERE LENGTH(first_name) = 4;

-- 4
SELECT *
FROM products
ORDER BY price ASC
LIMIT 5 OFFSET 5;

-- 5
SELECT *
FROM customers
WHERE joined_date < '2025-01-01' AND city != 'Uppsala'
ORDER BY city, last_name;
