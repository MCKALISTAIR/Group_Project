import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost",
							user = "root",
							passwd = "SEC09109!",
							db = "GroupProject")
	c = conn.cursor()
	
	return c, conn