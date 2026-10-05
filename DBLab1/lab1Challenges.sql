
-- Extra challenges

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
