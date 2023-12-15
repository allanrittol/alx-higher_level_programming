-- a script that lists all Comedy shows in the database
SELECT tv_shows.title
FROM tv_shows
JOIN show_genres ON tv_shows.id = show_genres.show_id
JOIN tv_genres ON show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
