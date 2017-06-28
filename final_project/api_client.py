import json
import tweepy
from db_connect import *

API_KEY = 'XRJqux8VbcklUvJclfjSUZqZx'
API_SECRET = 'TjqPBhE4GXXWutmvFTC29d01UfUTEuoLer7n6XzWhyZcA0A1cN'
TOKEN_KEY = '800864763261632512-pqrB1XJvlI9noWbbJa0AOQETjYPOIiz'
TOKEN_SECRET = 'ieUd260yCP29mgcxiSsI15DANmntMFs2PpUIERhbLOda1'

def get_api_instance():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
  api_inst = tweepy.API(auth)
  return api_inst

def do_data_pull(api_inst):

  sql_query = "select title from Movie"
  try:
    conn = create_connection()
    db_cursor = conn.cursor()
    query_status = run_stmt(db_cursor, sql_query)
    resultset = db_cursor.fetchall()

    for record in resultset:
      title = record[0]

      twitter_query = "(#" + title + " OR @" + title + ")"
      print "twitter_query: " + twitter_query
      twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en").items(50)

      for status in twitter_cursor:
          json_str = json.dumps(status._json)
          print "found a " + title + " tweet"
          insert_stmt = "insert into Tweet(tweet_doc, title) values(%s, %s)"
          run_prepared_stmt(db_cursor, insert_stmt, (json_str, title))
          do_commit(conn)

  except pymysql.Error as e:
    print "pymysql error: " + e.strerror



api_inst = get_api_instance()
do_data_pull(api_inst)
