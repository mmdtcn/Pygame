import random
import time
import socket
#words=['engineering','building','programming','python','streets','snacks']
words=['very','short','list']

# Networking
ip_address = "10.15.102.49" 
port=5555

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(words)

random.shuffle(words)
#print(words)

sentence="".join(words)
print(sentence)
start_time=time.time()

response=input("Enter the words")


end_time=time.time()

if sentence==response:
    elapsed_seconds=end_time - start_time
    print(f"Elapsed seconds {elapsed_seconds}")
    out = f"MMD WPM: {(len(sentence)/5)/elapsed_seconds*60}"
    print(out)
    s.sendto(out.encode('ascii'),(ip_address,port))
else:
    print("You need to practice more!")
    s.sendto("MMD can't type".encode('ascii'),(ip_address,port))
