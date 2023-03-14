-- A script that lists all records of the table
-- lists without row names are listed
-- listings in descending order

SELECT score, name FROM second_table WHERE LENGTH(name) > 0 ORDER BY score DESC;
