# Import pickle for saving state & sending info to network scoreboard
import pickle
# Import socket for sending score to scoreboard
import socket

file_name = 'saves.data'

def printScores(data):
    data = sorted(data, key=lambda a: a['score'])
    print(f"High Score: {data[0]['score']:0.2} by {data[0]['name']}")
    for object in data[:10]:
        print(f"  {object['score']:0.2}  {object['name']}")

def updateScore(name, score):
    print(f"Reaction time {score:0.3}")
    data = []
    try:
        data = pickle.load(open(file_name, "rb"))
    except :
        # error on load
        print('Save file doesnt exist or other error')
    best = None
    if len(data) > 0:
        best = min(map(lambda a: a['score'], data))
        if score < best:
            print("New high score!!")
    data.append( {'name': name, 'score':score} )    
    pickle.dump(data, open(file_name, "wb"))
    printScores(data)