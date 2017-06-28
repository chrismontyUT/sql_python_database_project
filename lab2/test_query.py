import pymysql
from db_connect import *

def test_query():

    results1 = ()
    results2 = ()

    is_success = True
    full_query = "select * from Instructor"
    query_frame = "select * from Instructor where instructor_type = %s"

    try:

        connection = create_connection()
        cursor = connection.cursor()

        query_status = run_stmt(cursor, full_query)
        if query_status is False:
            is_success = False

        results1 = cursor.fetchall()
        #print results1

        commit_status = do_commit(connection)
        if commit_status is False:
            is_success = False

    except pymysql.err as e:
        is_success = False
        print "test full query Error: " + e.strerror

    try:
        connection = create_connection()
        cursor = connection.cursor()

        cond = raw_input("What type of instructor do you want? ").strip()
        params = (cond)
        query_status = run_prepared_stmt(cursor, query_frame, params)
        if query_status is False:
            is_success = False

        results2 = cursor.fetchall()
        #print results2

    except pymysql.Error as e:
        is_success = False
        print "test prepared query Error: " + e.strerror

    print ""
    print "Query 1 results: "
    for row in results1:
        print row

    print ""
    print "Query 2 results: "
    for row in results2:
        print row

    print ""

    return is_success

test_query()
