import socket
import selectors
import types
import sys
from database import *

localIP = "0.0.0.0"
localPort = 20001


def accept_new_client(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def old_client_io(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print(f"From <{data.addr}>:", recv_data.decode())
            # data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


sel = selectors.DefaultSelector()
# Create a datagram socket
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as serversoc:
    # Bind to address and ip
    serversoc.bind((localIP, localPort))
    serversoc.listen()
    print("TCP server up and listening")
    serversoc.setblocking(False)
    sel.register(serversoc, selectors.EVENT_READ, data=None)
    sel.register(sys.stdin, selectors.EVENT_READ, data=None)


    # Listen for incoming clients
    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.fileobj == sys.stdin:
                    inputs = sys.stdin.readline()[:-1].split()
                    ip = inputs[0]
                    port = int(inputs[1])
                    msg = ' '.join(inputs[2:])
                    for key in sel.get_map().values():
                        if key.data is not None and key.data.addr == (ip, port):
                            key.data.outb += msg.encode()
                elif key.data is None:
                    # a new client is connecting
                    accept_new_client(key.fileobj)
                else:
                    # an old client is speaking
                    old_client_io(key, mask)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()