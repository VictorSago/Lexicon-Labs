
-- Day 1 Extra challenges

-- 1
SELECT *
FROM products
WHERE category != 'Accessories' 
	AND stock > 0
	AND name LIKE '% %'
ORDER BY category, price DESC;

-- 2
SELECT *
FROM customers
WHERE city LIKE 'S%' 
	OR city LIKE 'M%' 
	OR city IS NULL;

-- 3
SELECT *
FROM products
WHERE category = 'Shoes'
ORDER BY price DESC
LIMIT 1 OFFSET 1;

-- 4
SELECT *
FROM customers
WHERE joined_date LIKE '2024%'
	OR joined_date LIKE '2025%'
ORDER BY joined_date DESC
LIMIT 3;

-- 4 Alternative
SELECT *
FROM customers
WHERE strftime('%Y', joined_date) IN ('2024', '2025')
ORDER BY joined_date DESC
LIMIT 3;

-- 5
SELECT first_name || ' ' || last_name AS full_name
FROM customers
ORDER BY last_name;

-- 6
SELECT *,
       CASE
         WHEN price < 200 THEN 'budget'
         WHEN price < 800 THEN 'mid'
         ELSE 'premium'
       END AS price_level
FROM products;

-- 7
SELECT first_name, COALESCE(city, 'Unknown') AS city
FROM customers;

-- 8
SELECT *
FROM customers
WHERE strftime('%m', joined_date) <= '06';

-- 9
SELECT * FROM products
ORDER BY LENGTH(name) DESC
LIMIT 1;

-- 10
SELECT substr(email, 1, instr(email, '@') - 1) AS username
FROM customers;

-- 11
SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- 12
SELECT name || ' costs ' || CAST(price AS INTEGER) || ' kr' AS price_list
FROM products
WHERE stock > 0
ORDER BY price DESC;

-- 13
SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;

-- 13 Improved
SELECT COALESCE(city, 'Unknown') as city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;
