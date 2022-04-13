import socket
import sys
import selectors
import types
from Database.database import *

# serverAddressPort = ("192.168.50.31", 20001)
bufferSize = 1024

# Create a UDP socket at client side
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as clientsoc:
	status = input('Do you want to be discovered? ')

	# Send to server using created TCP socket
	if status == 'yes':
		name = input('Who do you want to talk to? ')
		try:
			ip, port = get_ip(name)
		except:
			print('The person you want to chat is not in address book, please add it')
			ip = input('please enter his/her ip address: ')
			port = input('please enter his/her port: ')
			create_user(name, ip, port)

		msgs = msg_sending()
		clientsoc.connect((ip, int(port)))
		for msg in msgs:
			clientsoc.send(msg.encode())

		sel = selectors.DefaultSelector()
		clientsoc.setblocking(False)
		sel.register(clientsoc, selectors.EVENT_READ, data=None)
		sel.register(sys.stdin, selectors.EVENT_READ, data=None)

		print('Begin Chatting')
		try:
			while True:
				events = sel.select(timeout=None)
				for key, mask in events:
					if key.fileobj == sys.stdin:
						# there is an input from terminal
						msg = sys.stdin.readline()[:-1]
						clientsoc.send(msg.encode())
						insert_sender(name, msg, 'sent')
					else:
						# socket received message
						msg = clientsoc.recv(bufferSize)
						print(f"<Server>: {msg.decode()}")
						msg_received(name, msg)
		except KeyboardInterrupt:
			print("Caught keyboard interrupt, exiting")
		finally:
			sel.close()

	else:
		name = input('Who do you want to talk to? ')
		for line in sys.stdin:
			try:
				insert_sender(name, line, 'pending')
			except:
				print('The person you want to chat is not in address book, please add it')
				ip = input('please enter his/her ip address: ')
				port = input('please enter his/her port: ')
				create_user(name, ip, port)
