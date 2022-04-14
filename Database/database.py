import pymysql
import time

password = "*****"

def create_user(name, ip, port, password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = "insert into user (name, ip, port) values(%s, %s, %s)"
	cursor.execute(sql, (name, ip, port))
	db.commit()
	db.close()


def get_ip(name, password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = "select * from user where name = %s"
	cursor.execute(sql, (name))
	result = cursor.fetchone()
	db.commit()
	db.close()
	return result[1], result[2]


def insert_sender(name, message, status, password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = "insert into sender (ip, port, name, message, status, time) values(%s, %s, %s, %s, %s, %s)"
	ip, port = get_ip(name)
	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, port, name, message, status, current_time))
	db.commit()
	db.close()


def msg_sending(password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = "select * from sender where status = 'pending'"
	cursor.execute(sql)
	results = cursor.fetchall()

	out = []
	for row in results:
		out.append(row[3])
		sql = "update sender set status = 'sent' where name = %s and message = %s"
		cursor.execute(sql, (row[2], row[3]))

	db.commit()
	db.close()
	return out


def msg_received(name, message, password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = "insert into receiver (ip, port, name, message, status, time) values(%s, %s, %s, %s, %s, %s)"
	ip, port = get_ip(name)
	current_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()) 
	cursor.execute(sql, (ip, port, name, message, 'received', current_time))
	db.commit()
	db.close()



	

	
