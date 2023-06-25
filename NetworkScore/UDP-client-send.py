import socket

port_number = 5555
ip_address = '10.17.102.208'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	message = input("Give me some text")

	s.sendto(message.encode('ascii'), (ip_address, port_number))
	print("Sent!")
	#(msg, addr) = s.recvfrom(1024)
	#msg = msg.decode('ascii')
	#print(msg)