-- Lists all genres of the database hbtn_0d_tvshows that are not linked
-- to the show Dexter, sorted in ascending order by genre name.
SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`
LEFT JOIN `tv_shows` AS t
ON s.`show_id` = t.`id`
WHERE t.`title` <> 'Dexter' OR t.`title` IS NULL
ORDER BY g.`name` ASC;
