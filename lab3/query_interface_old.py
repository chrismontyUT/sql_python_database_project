import pymysql
from db_connect import *

def print_menu():
    print "1. Show movies greater than a certain rating"
    print "2. Show movies released in a ceratin year"
    print "3. Show each user rating that has at least 10 movies, and how many movies that rating has"
    print "4. Show each sound system in the database"
    print "5. Show average proce of a dvd of a chosen MPAA rating"
    print "6. Show all of the movies, when they were made, and their genres"
    print "7. Show all movies, their user rating, and their directors"
    print "8. Show all Dvds and the studios that made them"
    print "9. Show all movies with a certain MPAA rating and higher than a chosen rating."
    print "10.Show Dvds of a chosen MPAA rating below a chosen price "
    print "11. use movie_genre view"
    print "12. use dvd_studio view"
    print "13. exit"
def view_movie_genre_menu():
    print "1. Show how many movies in each genre"
    print "2. View all movies of a certain genre"

def view_dvd_studio_menu():
    print "1. Show all dvds below a chosen price "
    print "2. Show all dvds made by a chosen studio"
    print "3. Show how many dvds are made by each studio"

def movie_above_a_rating():

   is_success = True

   query_frame = "select title, imdb_user_rating from Movie where  imdb_user_rating  >= %s  ORDER BY imdb_user_rating"

   try:
        connection = create_connection()
        cursor = connection.cursor()
        rating = raw_input("Enter a rating between one and ten reported to one decimal place: ").strip()
        while rating == "; drop table" or rating == "; truncate table" or rating == "; delete from" or rating == "or 1=1":
            print "SQL injection detected, input aborted"
            rating = raw_input("Enter a rating between one and ten reported to one decimal place: ").strip()

        rating= float(rating)
        while rating > 10 or rating < 0:
            rating = input("Try again:")
        params = (rating)

        query_status = run_prepared_stmt(cursor, query_frame, params)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

   except pymysql.Error as e:
        is_success = False
        print "movie query failed: " + e.strerror

   return is_success

def movie_made_a_year():

   is_success = True

   query_frame = "select title from Movie where release_year = %s ORDER BY title"

   try:
        connection = create_connection()
        cursor = connection.cursor()
        year = raw_input("Enter a year: ").strip()
        while year == "; drop table" or year == "; truncate table" or year == "; delete from" or year == "or 1=1":
            print "SQL injection detected, input aborted"
            year = raw_input("Enter a year: ").strip()
        year= int(year)
        while year > 2016 or year < 1900:
            year = input("Try again:")
        params = (year)

        query_status = run_prepared_stmt(cursor, query_frame, params)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

   except pymysql.Error as e:
        is_success = False
        print "movie query failed: " + e.strerror
   return is_success

def number_of_a_rating():

       is_success = True

       query_frame = "select imdb_user_rating, COUNT(*) how_many from Movie GROUP BY imdb_user_rating HAVING COUNT(*) > 10"

       try:
            connection = create_connection()
            cursor = connection.cursor()



            query_status = run_stmt(cursor, query_frame)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

       except pymysql.Error as e:
            is_success = False
            print "movie query failed: " + e.strerror
       return is_success

def list_sound():

    is_success = True

    query_frame = "select DISTINCT sound, count(*) how_many FROM Dvd GROUP BY sound HAVING count(*) > 10"

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_stmt(cursor, query_frame)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "Dvd query failed: " + e.strerror
    return is_success

def avg_price():
     is_success = True

     query_frame = "select AVG(price) avg_price FROM Dvd WHERE rating = %s"

     try:
          connection = create_connection()
          cursor = connection.cursor()
          rating = raw_input("Enter an MPAA rating: ").strip()
          while rating == "; drop table" or rating == "; truncate table" or rating == "; delete from" or rating == "or 1=1":
              print "SQL injection detected, input aborted"
              rating = raw_input("Enter an MPAA rating: ").strip()
          rating = str(rating)

          params = (rating)

          query_status = run_prepared_stmt(cursor, query_frame, params)
          if query_status is False:
              is_success = False

          results = cursor.fetchall()
          print ""
          for row in results:
              print row
          print ""

     except pymysql.Error as e:
          is_success = False
          print "DVD query failed: " + e.strerror
     return is_success

def movie_and_genre():
   is_success = True

   query_frame = "select a.title, a.release_year, g.genre_name FROM Movie a INNER JOIN Genre_Junction_Table g ON a.title = g.title ORDER BY g.genre_name"

   try:
        connection = create_connection()
        cursor = connection.cursor()



        query_status = run_stmt(cursor, query_frame)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

   except pymysql.Error as e:
        is_success = False
        print "movie query failed: " + e.strerror
   return is_success

def movie_and_director():
       is_success = True

       query_frame = "select a.title, a.imdb_user_rating, d.director_name FROM Movie a INNER JOIN Director_Junction_Table d ON a.title = d.title ORDER BY a.imdb_user_rating DESC"

       try:
            connection = create_connection()
            cursor = connection.cursor()



            query_status = run_stmt(cursor, query_frame)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

       except pymysql.Error as e:
            is_success = False
            print "movie query failed: " + e.strerror
       return is_success

def dvd_and_studio():
       is_success = True

       query_frame = "select d.title, s.studio FROM Dvd d INNER JOIN Studio_Junction_Table s ON d.title = s.title ORDER BY d.title"

       try:
            connection = create_connection()
            cursor = connection.cursor()



            query_status = run_stmt(cursor, query_frame)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

       except pymysql.Error as e:
            is_success = False
            print "DVD query failed: " + e.strerror
       return is_success

def right_outer_dvd_movie():

   is_success = True

   query_frame = "select d.title, a.imdb_user_rating, d.rating from Movie a RIGHT OUTER JOIN dvd d ON a.title = d.title where  a.imdb_user_rating  >= %s  and d.rating = %s"

   try:
        connection = create_connection()
        cursor = connection.cursor()
        user_rating = raw_input("Enter a user rating (between 0 and 10) to show movies greater than that rating: ")
        while user_rating == "; drop table" or user_rating == "; truncate table" or user_rating == "; delete from" or user_rating == "or 1=1":
            print "SQL injection detected, input aborted"
            user_rating = raw_input("Enter a user rating (between 0 and 10) to show movies greater than that rating: ").strip()
        user_rating = float(user_rating)
        while user_rating > 10 or user_rating < 0:
            user_rating = raw_input("Try again")
        rating = raw_input("Enter a MPAA rating: ").strip()
        rating= str(rating)

        params = (user_rating , rating)

        query_status = run_prepared_stmt(cursor, query_frame, params)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

   except pymysql.Error as e:
        is_success = False
        print "movie query failed: " + e.strerror

   return is_success

def full_outer_dvd_movie():

   is_success = True

   query_frame = "select a.title, a.imdb_user_rating, d.rating, d.price FROM Movie a LEFT JOIN dvd d ON a.title = d.title UNION select a.title, a.imdb_user_rating, d.rating, d.price FROM MOVIE a RIGHT JOIN dvd d ON a.title = d.title WHERE d.rating = %s and d.price < %s"


   try:
        connection = create_connection()
        cursor = connection.cursor()
        price = raw_input("Enter a price (greater than 0) to show dvds below that price: ")
        while price == "; drop table" or price == "; truncate table" or price == "; delete from" or price == "or 1=1":
            print "SQL injection detected, input aborted"
            price = raw_input("Enter a price (greater than 0) to show dvds below that price: ").strip()
        price = float(price)
        while  price < 0:
            price = raw_input("Try again")
        rating = raw_input("Enter a MPAA rating: ").strip()
        rating = str(rating)

        params = (rating , price)

        query_status = run_prepared_stmt(cursor, query_frame, params)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

   except pymysql.Error as e:
        is_success = False
        print "movie query failed: " + e.strerror

   return is_success
######## functions for views below


def how_many_in_a_genre():

    is_success = True

    query_frame = "select genre, COUNT(*) how_many FROM movie_genre GROUP BY genre"

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_stmt(cursor, query_frame)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "movie_genre view query failed: " + e.strerror
    return is_success

def movies_by_genre():
       is_success = True

       query_frame = "select title from movie_genre WHERE genre = %s ORDER BY title"

       try:
            connection = create_connection()
            cursor = connection.cursor()
            genre = raw_input("Enter a genre (Action, Crime , ect.) : ").strip()
            while genre == "; drop table" or genre == "; truncate table" or genre == "; delete from" or genre == "or 1=1":
                print "SQL injection detected, input aborted"
                genre = raw_input("Enter a genre (Action, Crime , ect.) : ").strip()

            params = (genre)

            query_status = run_prepared_stmt(cursor, query_frame, params)
            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

       except pymysql.Error as e:
            is_success = False
            print "movie_genre view query failed: " + e.strerror
       return is_success

def dvds_below_a_price():

    is_success = True

    query_frame = "select title, price FROM dvd_studio WHERE price < %s ORDER BY title"

    try:
        connection = create_connection()
        cursor = connection.cursor()

        price = raw_input("Enter the maximum price desired: ").strip()
        while price == "; drop table" or price == "; truncate table" or price == "; delete from" or price == "or 1=1":
            print "SQL injection detected, input aborted"
            price = raw_input("Enter the maximum price desired: ").strip()
        price = float(price)
        while price < 0:
            price = raw_input("Try again: ")
        params = (price)
        query_status = run_prepared_stmt(cursor, query_frame, params)

        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "dvd_studio view query failed: " + e.strerror
    return is_success

def dvd_by_studio():
        is_success = True

        query_frame = "select title, studio FROM dvd_studio WHERE studio = %s ORDER BY title"

        try:
            connection = create_connection()
            cursor = connection.cursor()

            studio = raw_input("Enter desired studio (Lions Gate, Fox , ect.): ").strip()
            while studio == "; drop table" or studio == "; truncate table" or studio == "; delete from" or studio == "or 1=1":
                print "SQL injection detected, input aborted"
                studio = raw_input("Enter desired studio (Lions Gate, Fox , ect.): ").strip()

            params = (studio)
            query_status = run_prepared_stmt(cursor, query_frame, params)

            if query_status is False:
                is_success = False

            results = cursor.fetchall()
            print ""
            for row in results:
                print row
            print ""

        except pymysql.Error as e:
            is_success = False
            print "dvd_studio view query failed: " + e.strerror
        return is_success

def num_dvds_per_studio():

    is_success = True

    query_frame = "select studio, COUNT(*) how_many FROM dvd_studio GROUP BY studio"

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_stmt(cursor, query_frame)
        if query_status is False:
            is_success = False

        results = cursor.fetchall()
        print ""
        for row in results:
            print row
        print ""

    except pymysql.Error as e:
        is_success = False
        print "movie_studio view query failed: " + e.strerror
    return is_success









while True:
    print " "
    print_menu()
    print " "
    choice = input("Enter your choice [1-13]: ")
    print " "

    if choice==1:
        print "You have chosen to view movies above a certain rating "
        print " "
        movie_above_a_rating()
    elif choice==2:
        print "You have chosen to show movies made a certain year "
        print " "
        movie_made_a_year()
    elif choice==3:
        print "You have chosen to show the user ratings that have at least 10 movies with that rating: "
        print " "
        number_of_a_rating()

    elif choice==4:
        print "You have chosen to see all sound systems in the database."
        print " "
        list_sound()

    elif choice == 5:
        print "You have chosen to see the average price of movies with a certain MPAA rating"
        print " "
        avg_price()

    elif choice == 6:
        print "You have chosen to see all movies, when they were made, and their respective genres."
        print " "
        movie_and_genre()

    elif choice == 7:
        print " You have chosen to see all movies, their user ratings, and their directors"
        print " "
        movie_and_director()

    elif choice == 8:
        print "You have chosen to see all Dvds and the studios that made them"
        print " "
        dvd_and_studio()

    elif choice == 9:
        print "you have chosen to view all movies with a chosen MPAA rating higher than a chosen user_rating."
        print " "
        right_outer_dvd_movie()
    elif choice == 10:
        print "You have chosen to see all DVDs of a chosen MPAA rating below a chosen price"
        print " "
        full_outer_dvd_movie()

    elif choice == 11:
        print " "
        view_movie_genre_menu()
        print " "
        new_choice = input("Enter your choice [1-2]: ")
        print " "
        if new_choice == 1:
            print "You have chosen to view how many movies are in each genre"
            print " "
            how_many_in_a_genre()
        elif new_choice == 2:
            print "You have chosen to view all movies of a chosen genre."
            print " "
            movies_by_genre()


    elif choice == 12:
        print " "
        view_dvd_studio_menu()
        print " "
        new_choice = input("Enter your choice [1-3]: ")
        print " "
        if new_choice == 1:
            print "You have chosen to see all dvds below a chosen price."
            print " "
            dvds_below_a_price()
        elif new_choice == 2:
            print "You have chosen to see all movies made by a studio of your choosing."
            print " "
            dvd_by_studio()
        elif new_choice == 3:
            print "You have chosen to see how many dvds each studio has produced."
            print " "
            num_dvds_per_studio()
    elif choice == 13:
        print "goodbye!"
        break
    else:
        raw_input("Wrong choice! Try again: ")
