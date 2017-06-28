import pymysql
import csv
from db_connect import *

def import_Studio_Junction_Table():
    is_success = True
    insert_prefix = "insert into Studio_Junction_Table (title, studio) values ("


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
                if j == 0:
                    insert_stmt += "'" + val + "', "
                #elif j == 2:
                    continue
                elif j == 1:
                    val = val.split("/")
                    for i in val:
                        i = i.strip()
                        i = i.lower()
                        new_insert_stmt = insert_stmt + "'" + i + "'" + ")"
                        #print(new_insert_stmt)
                        insert_status = cursor.execute(new_insert_stmt)
                        new_insert_stmt = insert_stmt

                else:
                    continue
                    #insert_stmt += "str_to_date('" + val + "','%m/%d/%Y')"

            if insert_status is False:
                is_success = False
                return is_success
        commit_status = connection.commit()
        if commit_status is False:
        	is_success = False
        	return is_success
    except pymysql.err as e:
        is_success = False
        print "import_Studio_Junction_Table Error: " + e.strerror

    return is_success
