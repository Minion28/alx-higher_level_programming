-- List all cities of CA found in db 'hbtn_0d_usa' with cities in ascending order 
SELECT id, name FROM cities WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California'
);
