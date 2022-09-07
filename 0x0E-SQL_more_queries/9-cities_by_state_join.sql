-- List all cities in db 'hbtn_0d_usa' using SELECT
SELECT cities.id, cities.name, states.name FROM states INNER JOIN cities ON states.id = cities.state_id;
