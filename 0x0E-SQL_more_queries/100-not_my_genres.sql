-- Retrieves a list of all genres that are not linked to the show Dexter.
-- The tv_shows table contains only one record with a title of "Dexter" (the id may vary).
-- Each record will display the name of the genre from the tv_genres table.
-- The results will be sorted in ascending order by the genre name.
-- A maximum of two SELECT statements can be used.
-- The database name will be provided as an argument in the mysql command.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN
(SELECT tv_genres.id
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
