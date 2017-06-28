import pymysql
import csv
from db_connect import *

def import_Dvd():
    is_success = True
    insert_prefix = "insert into dvd (title,sound, price, rating,release_date) values ("


    try:

        connection = create_connection()
        cursor = connection.cursor()

        csvfile = open("dvd.csv", "rb")
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0: continue

            insert_stmt = insert_prefix
            for j, val in enumerate(row):
                val = val.replace("'" , "\\'")
                if j == 0 or j == 5 or j == 6 or j == 7:
                    insert_stmt += "'" + val + "', "
                #elif j == 2:
                    continue
                elif j == 12:
                    insert_stmt += "'" + val + "'"
                else:
                    continue
                    #insert_stmt += "str_to_date('" + val + "','%m/%d/%Y')"
            insert_stmt += ")"
            #print(insert_stmt)
            insert_status = cursor.execute(insert_stmt)
            if insert_status is False:
                is_success = False
                return is_success
        commit_status = connection.commit()
        if commit_status is False:
            is_success = False
            return is_success
    except pymysql.err as e:
        is_success = False
        print "import_Movie Error: " + e.strerror

    return is_success
