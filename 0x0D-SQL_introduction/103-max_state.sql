-- display max temperatre of each city

SELECT state, max(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;

