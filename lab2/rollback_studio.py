import pymysql
from db_connect import *


def rollback_studio():
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute("delete from studio")
		conn.commit()

	except pymysql.Error as error:
		print "connection error", error
	return True
