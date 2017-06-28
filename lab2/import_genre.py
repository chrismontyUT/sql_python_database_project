import pymysql
import csv
from db_connect import *

def import_genre():

	is_success = True
	insert_stmt = "insert into Genre (genre_name) values (%s)"
	genre_list = []
	try:

		connection = create_connection()
		cursor = connection.cursor()

		csvfile = open("watchlist.csv", "rb")
		reader = csv.reader(csvfile)
		for i, row in enumerate(reader):
			if i == 0:
				continue
			for j, val in enumerate(row):
				val = val.replace("'" , "\\'")
				val = val.replace(" " , "")
				if j == 12:
					val = val.split(",")
					for i in val:
						if i in genre_list:
							continue
						else:
							genre_list.append(i)
				else:
					continue
		#print(genre_list)
		for i in genre_list:
			insert_status = cursor.execute(insert_stmt, (i))
		if insert_status is False:
			is_success = False
		connection.commit()


	except pymysql.err as e:
		print "import_Genre error: " + e.strerror
		is_success = False
	return is_success
