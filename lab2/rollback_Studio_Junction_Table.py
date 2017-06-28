import pymysql
from db_connect import *

def rollback_Studio_Junction_Table():
	try:
		conn = create_connection()
		cur = conn.cursor()
		cur.execute("delete from studio_junction_table")
		conn.commit()

	except pymysql.Error as error:
		print "connection error", error
	return True
