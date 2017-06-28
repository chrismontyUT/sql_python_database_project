import pymysql
from db_connect import *


def rollback_Dvd():
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute("delete from dvd")
		conn.commit()

	except pymysql.Error as error:
		print "connection error", error
	return True
