-- Retrieves a list of all Comedy shows in the hbtn_0d_tvshows database.
-- The tv_genres table contains only one record with a genre name of "Comedy" (the id may vary).
-- Each record will display the title of the tv show.
-- The results will be sorted in ascending order by the show title.
-- Only one SELECT statement is allowed.
-- The database name will be provided as an argument in the mysql command.

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
