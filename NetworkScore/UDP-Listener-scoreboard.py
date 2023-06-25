import socket
import pickle

high_scores = {}
def print_scores(scores):
	if len(scores) == 0:
		print("No scores yet")
		return
	pairs = scores.items()
	pairs = sorted(pairs, key=lambda a: -a[1])
	print()
	print(f"Max score: {pairs[0][0]} with {pairs[0][1]:.1f}")
	print()
	for name,score in pairs:
		print(f"{name}: {score:.1f}")


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
	try:
		msg2 = msg.decode('ascii')
		print("Got '{}' from {}".format(addr, msg2))
	except:
		thing = pickle.loads(msg)
		try:
			high_scores[thing['name']] = thing['score']
			print_scores(high_scores)
		except:
			print(f"Invalid pickle {thing}")
	





print(msg)