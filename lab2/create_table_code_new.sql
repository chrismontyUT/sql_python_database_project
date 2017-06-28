drop database if exists IMDB;
create database IMDB;
use IMDB;

CREATE TABLE Movie (
  title varchar(200) primary key,
  release_year integer not null,
  runtime_in_minutes integer not null,
  imdb_user_rating float not null,
  number_of_user_votes integer not null
);
CREATE TABLE Studio (
   studio varchar(200) primary key
 );  

CREATE TABLE Dvd (
   title varchar(200) primary key,
   release_date varchar(200)not null,
   sound varchar(200) not null,
   price float not null,
   rating varchar(200) not null
);

CREATE TABLE Studio_Junction_table (
  title varchar(200) not null,
  studio varchar(200) not null,
  CONSTRAINT PK_Studio_Junction_Table primary key
  ( 
     title,
	 studio
   ),

   foreign key(title) REFERENCES Dvd(title),
   foreign key(studio)REFERENCES Studio(studio)
);

CREATE TABLE Genre (
  genre_name varchar(200) primary key
);

CREATE TABLE Genre_Junction_Table (
  genre_name varchar(200) not null,
  title varchar(200) not null,
  CONSTRAINT PK_Genre_Junction_Table primary key
  (
    title,
    genre_name
  ),

  FOREIGN KEY (title) REFERENCES Movie(title),
  FOREIGN KEY (genre_name) REFERENCES Genre(genre_name)
);


CREATE TABLE Director (
  director_name varchar(200) primary key
);

CREATE TABLE Director_Junction_Table (
  title varchar(200) not null,
  director_name varchar(200) not null,
  CONSTRAINT PK_Director_Junction_Table primary key
  (
    title,
    director_name
  ),

  FOREIGN KEY(title) REFERENCES Movie(title),
  FOREIGN KEY(director_name) REFERENCES Director(director_name)
);


   


