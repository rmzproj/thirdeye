import mysql.connector
def select(q):
	cnx = mysql.connector.connect(user='root',password='',host='localhost',database='project_eye')
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	res = cur.fetchall()
	return res

def update(q):
	cnx = mysql.connector.connect(user='root',password='',host='localhost',database='project_eye')
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	res = cur.rowcount
	return res
	
def insert(q):
	cnx = mysql.connector.connect(user='root',password='',host='localhost',database='project_eye')
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	res = cur.lastrowid
	return res