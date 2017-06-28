import pymysql
import csv
from db_connect import *

def import_Movie():
    is_success = True
    insert_prefix = "insert into movie (title,imdb_user_rating,runtime_in_minutes, release_year,number_of_user_votes) values ("


    try:

		connection = create_connection()
        cursor = connection.cursor()

        csvfile = open("watchlist.csv", "rb")
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0: continue

            insert_stmt = insert_prefix
            for j, val in enumerate(row):
                val = val.replace("'" , "\\'")
                if j == 5 or j == 9 or j == 10 or j == 11:
                    insert_stmt += "'" + val + "', "
                #elif j == 2:
                    continue
                elif j == 13:
                    insert_stmt += "'" + val + "'"
                else:
                    continue
                    #insert_stmt += "str_to_date('" + val + "','%m/%d/%Y')"
            insert_stmt += ")"
            #print(insert_stmt)
            insert_status = cursor.execute(insert_stmt)
            if insert_status is False:
                is_success = False
        connection.commit()

    except pymysql.err as e:
        is_success = False
        print "import_Movie Error: " + e.strerror
    return is_success
