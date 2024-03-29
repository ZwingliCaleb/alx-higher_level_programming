-- write a script that lists all genres in the database by their ratings each record should display tv_genres.name - rating sum and results must be sorted in descending order

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
	FROM tv_genres
	JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	JOIN tv_show_ratings
	ON tv_shows.id = tv_show_ratings.show_id
	GROUP BY tv_genres.name
	ORDER BY rating DESC;
