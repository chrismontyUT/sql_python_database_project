import pymysql
import csv
from db_connect import *

def import_Director():

	is_success = True
	insert_stmt = "insert into Director (director_name) values (%s)"
	dir_list = []
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
				val = val.strip()
				if j == 7:
					val = val.split(",")
					for i in val:
						i = i.strip()
						if i in dir_list:
							continue
						else:
							dir_list.append(i)
							#print(i)


				else:
					continue
		#print(dir_list)
		for i in dir_list:
			insert_status = cursor.execute(insert_stmt, (i))
		if insert_status is False:
			is_success = False

		commit_status = connection.commit()
		if commit_status is False:
			is_success = False

	except pymysql.err as e:
		print "import_Director error: " + e.strerror
		is_success = False
	return is_success
