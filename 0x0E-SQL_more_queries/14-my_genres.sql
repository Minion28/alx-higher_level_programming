-- Use 'hbtn_0d_tvshows' to list all genres of the show 'Dexter' using select
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres m ON tv_genres.id = m.genre_id INNER JOIN tv_shows s ON m.show_id = s.id WHERE s.title = 'Dexter' ORDER BY tv_genres.name ASC;
