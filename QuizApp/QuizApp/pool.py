import pymysql as MySql
import pymysql.cursors
def ConnectionPooling():
  DB=MySql.connect(host='localhost',passwd='varun',port=3306,user='root',database='quizregistration',cursorclass=MySql.cursors.DictCursor)
  CMD=DB.cursor()
  return DB,CMD
