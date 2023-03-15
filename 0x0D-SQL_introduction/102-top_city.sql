-- Write a script that displays the top 3 cities temperature during July and August ordered by temperature

SELECT city, AVG(value) AS avg_temp FROM teemperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
