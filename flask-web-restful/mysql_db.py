from flask_mysqldb import MySQL

MYSQL_HOST = '192.168.0.178'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'as1996'
MYSQL_DB = 'flaskdb'
MYSQL_CURSORCLASS = 'DictCursor'

# init MYSQL
mysql = MySQL()
