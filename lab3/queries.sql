CREATE VIEW dvd_studio
  (title, dvd_release_date, sound, price, rating, studio)
AS 
SELECT a.title, a.dvd_release_date, a.sound, a.price, a.rating, s.studio
FROM Dvd a
JOIN Studio_Junction_Table s ON a.title = s.title;

CREATE VIEW movie_genre
 (title,
  imdb_user_rating,
  runtime_in_minutes,
  release_year,
  number_of_user_votes,
  genre)
AS
SELECT a.title, a.imdb_user_rating, a.runtime_in_minutes, a.release_year, a.number_of_user_votes, g.genre_name
FROM Movie a
JOIN Genre_Junction_Table g ON a.title = g.title;

select title, imdb_user_rating 
from Movie 
where  imdb_user_rating  >= [8.1]  
ORDER BY imdb_user_rating;

select title 
from Movie 
where release_year = [2001] 
ORDER BY title;

select imdb_user_rating, COUNT(*) how_many 
from Movie 
GROUP BY imdb_user_rating 
HAVING COUNT(*) > 10;

select DISTINCT sound, count(*) how_many 
FROM Dvd 
GROUP BY sound 
HAVING count(*) > 10;

select AVG(price) avg_price 
FROM Dvd 
WHERE rating = [PG];

select a.title, a.release_year, g.genre_name 
FROM Movie a 
INNER JOIN Genre_Junction_Table g 
  ON a.title = g.title 
ORDER BY g.genre_name;

select a.title, a.imdb_user_rating, d.director_name 
FROM Movie a 
INNER JOIN Director_Junction_Table d 
   ON a.title = d.title 
ORDER BY a.imdb_user_rating DESC;

select d.title, s.studio 
FROM Dvd d 
INNER JOIN Studio_Junction_Table s 
  ON d.title = s.title 
ORDER BY d.title;

select d.title, a.imdb_user_rating, d.rating 
from Movie a 
RIGHT OUTER JOIN dvd d 
  ON a.title = d.title 
where  a.imdb_user_rating  >= [8.7]  and d.rating = [PG];

select a.title, a.imdb_user_rating, d.rating, d.price 
FROM Movie a 
LEFT JOIN dvd d 
  ON a.title = d.title 
UNION 
select a.title, a.imdb_user_rating, d.rating, d.price 
FROM MOVIE a 
RIGHT JOIN dvd d 
  ON a.title = d.title 
WHERE d.rating = [PG] and d.price < [20];

select genre, COUNT(*) how_many 
FROM movie_genre 
GROUP BY genre;

select title 
from movie_genre 
WHERE genre = [Action] 
ORDER BY title;

select title, price 
FROM dvd_studio 
WHERE price < [20] 
ORDER BY title;

select title, studio 
FROM dvd_studio 
WHERE studio = [Fox] 
ORDER BY title;

select studio, COUNT(*) how_many 
FROM dvd_studio 
GROUP BY studio;























