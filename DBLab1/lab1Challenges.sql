
-- Extra challenges

-- 1
SELECT *
FROM products
WHERE category != 'Accessories' 
	AND stock > 0
	AND name LIKE '% %'
ORDER BY category, price DESC;
