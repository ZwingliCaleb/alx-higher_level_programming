-- write a script to create a table where the id attribute is defaulted to 1 and the value is unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
