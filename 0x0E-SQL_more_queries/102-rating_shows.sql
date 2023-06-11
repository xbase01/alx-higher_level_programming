-- Retrieves a list of all shows from the hbtn_0d_tvshows_rate table, grouped by their rating sum.
-- Each record will display the title of the tv show from the tv_shows table and its corresponding rating sum.
-- The results will be sorted in ascending order by the rating sum.
-- The database name will be provided as an argument in the mysql command.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
