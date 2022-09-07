-- Create table 'unique_id' with description id default as 1 and name
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
