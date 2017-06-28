import pymysql
import csv
from db_connect import *

def import_Studio():

	is_success = True
	insert_stmt = "insert into Studio (studio) values (%s)"
	studio_list = []
	try:

		connection = create_connection()
		cursor = connection.cursor()

		csvfile = open("dvd.csv", "rb")
		reader = csv.reader(csvfile)
		for i, row in enumerate(reader):
			if i == 0:
				continue
			for j, val in enumerate(row):
				#val = val.replace("'" , "''")
				val = val.strip()
				val = val.lower()
				if j == 1:
					val = val.split("/")
					for i in val:
						i = i.strip()
						if i in studio_list:
							continue
						else:
							studio_list.append(i)


				else:
					continue
		studio_list.sort()
		#print(studio_list)
		for i in studio_list:
			insert_status = cursor.execute(insert_stmt, (i))
		if insert_status is False:
			is_success = False

		commit_status = connection.commit()
		if commit_status is False:
			is_success = False

	except pymysql.err as e:
		print "import_Studio error: " + e.strerror
		is_success = False
	return is_success
