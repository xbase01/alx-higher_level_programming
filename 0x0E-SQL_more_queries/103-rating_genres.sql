-- Retrieves a list of all genres from the hbtn_0d_tvshows_rate database, grouped by their rating sum.
-- Each record will display the name of the genre from the tv_genres table and its corresponding rating sum.
-- The results will be sorted in ascending order by the rating sum.
-- The database name will be provided as an argument in the mysql command.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
