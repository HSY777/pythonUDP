#server
import socket

port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", port))

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode().upper()
    sock.sendto(data.encode(), addr)

sock.close()