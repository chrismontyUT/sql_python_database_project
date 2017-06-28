select title, COUNT(*)
FROM Tweet
GROUP BY title;

select screen_name , COUNT(*)
from tweet
group by screen_name
Order BY COUNT(*) DESC;

select a.title, a.imdb_user_rating ,
(select COUNT(*) from Tweet WHERE title = a.title) as tweets
from Movie a
group by title
order by imdb_user_rating;

select a.title, a.runtime_in_minutes ,
(select COUNT(*) from Tweet WHERE title = a.title) as tweets
from Movie a
group by title
order by tweets desc;

select a.title, a.release_year ,
(select COUNT(*) from Tweet WHERE title = a.title) as tweets
from Movie a
WHERE a.release_year > 2010
group by title
order by release_year desc;