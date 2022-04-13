import pymysql
import time

password = "*****"
db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
cursor = db.cursor()


def create_user(name, ip, port):
	sql = "insert into user (name, ip, port) values(%s, %s, %s)"
	cursor.execute(sql, (name, ip, port))
	db.commit()


def get_ip(name):
	sql = "select * from user where name = %s"
	cursor.execute(sql, (name))
	result = cursor.fetchone()
	return result[1], result[2]


def insert_sender(name, message, status):
	sql = "insert into sender (ip, port, name, message, status, time) values(%s, %s, %s, %s, %s, %s)"
	ip, port = get_ip(name)
	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, port, name, message, status, current_time))
	db.commit()


def msg_sending():
	sql = "select * from sender where status = 'pending'"
	cursor.execute(sql)
	results = cursor.fetchall()

	out = []
	for row in results:
		out.append(row[3])
		sql = "update sender set status = 'sent' where name = %s and message = %s"
		cursor.execute(sql, (row[2], row[3]))

	db.commit()
	return out


def msg_received(name, message):
	sql = "insert into receiver (ip, port, name, message, status, time) values(%s, %s, %s, %s, %s, %s)"
	ip, port = get_ip(name)
	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, port, name, message, 'received', current_time))
	db.commit()



	

	
