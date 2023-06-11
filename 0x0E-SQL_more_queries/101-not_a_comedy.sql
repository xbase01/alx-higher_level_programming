-- Retrieves a list of all shows in the hbtn_0d_tvshows database that do not have the genre "Comedy".
-- The tv_genres table contains only one record with a genre name of "Comedy" (the id may vary).
-- Each record will display the title of the tv show from the tv_shows table.
-- The results will be sorted in ascending order by the show title.
-- A maximum of two SELECT statements can be used.
-- The database name will be provided as an argument in the mysql command.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_shows.id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
