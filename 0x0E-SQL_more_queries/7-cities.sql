-- Write a script that creates a database hbtn_0d_usa and table cities on server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	CONSTRAINT FOREIGN KEY (state_id) REFERRENCES states(id),
	name VARCHAR(256) NOT NULL);
