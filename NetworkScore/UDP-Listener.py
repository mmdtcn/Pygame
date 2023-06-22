import socket
import pickle


port_number = 5555
ip_address = '0.0.0.0'

hostname = socket.gethostname()
my_address = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (ip_address, port_number) )

print(f"Listening on {my_address} port {port_number}")

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	msg2 = msg.decode('ascii')
	print("Got '{}' from {}".format(addr, msg2))

	