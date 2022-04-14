import pymysql
import time

password = "*****"

def create_user(password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = 'drop table if exists user'
	cursor.execute(sql)

	sql = 'create table user (name VARCHAR(40), ip VARCHAR(40), port VARCHAR(20))'
	cursor.execute(sql)

	db.commit()
	db.close()
	
	
def create_sender(password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = 'drop table if exists sender'
	cursor.execute(sql)

	sql = 'create table sender (ip VARCHAR(40), port VARCHAR(20), name VARCHAR(40), message TEXT, status VARCHAR(20), time VARCHAR(40))'
	cursor.execute(sql)

	db.commit()
	db.close()
	
	
def create_receiver(password = password):
	db = pymysql.connect(host = "localhost", user = "root", password = password, database = "peer_to_peer_chat")
	cursor = db.cursor()
	sql = 'drop table if exists receiver'
	cursor.execute(sql)

	sql = 'create table receiver (ip VARCHAR(40), port VARCHAR(20), name VARCHAR(40), message TEXT, status VARCHAR(20), time VARCHAR(40))'
	cursor.execute(sql)

	db.commit()
	db.close()
	
create_user()
create_sender()
create_receiver()
