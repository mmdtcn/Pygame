import random
import time

#words=['engineering','building','programming','python','streets','snacks']
words=['very','short','list']


print(words)

random.shuffle(words)
#print(words)

sentence="".join(words)
print(sentence)
start_time=time.time()

response=input("Enter the words")


end_time=time.time()

if sentence==response:
    print(f"Elapsed seconds {end_time - start_time}")
    print(f"WPM: {len(sentence)/5}")
else:
    print("You need to practice more!")