import random
import time
import socket
import pickle

port = 5555
ip = "10.15.102.49"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

words = ['the','camp','shop','computer','metal','wood']
words = ['the','camp']

#print(words)

random.shuffle(words)

#print(words)

paragraph = " ".join(words)

#print(paragraph)
ready = input("Ready to go?")

print(paragraph)
start_time = time.time()

response = input("Type the words above: ")
end_time = time.time()

message = ""
if response == paragraph:
	print("Correct!")
	elapsed = end_time - start_time
	print(f"It took you {elapsed} seconds!")
	print(f"That is {len(words) / elapsed * 60} words per minute!")
	message = f"Paul WPM:{len(words) / elapsed * 60}"

else:
	print("Incorrect typing")
	message = "Paul needs more work"

s.sendto(message.encode('ascii'), (ip, port))