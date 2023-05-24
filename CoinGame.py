'''
import random
def coinToss():
    coin = random.choice(['H','T'])
    return coin

def coinGame():
    coin = coinToss()
    coin+=coinToss()
    player1 = 0
    player2 = 0
    while player1==0 and player1==0:
        coin+=coinToss()
        if coin[-3:] == 'HHT':
            player1+=1
            return 'player1'
        if coin[-3:] == 'HTH':
            player2+=1
            return 'player2'
        
def coinGameOutcome(trials):
    player1 = 0
    player2 = 0
    for _ in range(trials):
        result = coinGame()
        if result=='player1':
            player1+=1
        else:
            player2+=1
    per1 = player1/trials
    per2 = player2/trials
    print(per1*100, per2*100)

coinGameOutcome(100000)
'''

import random
def headTails():
    rosen = "THH"
    student = "HHT"
    outcomes = ["H","T"]
    results = {}
    for i in range(100000):
        flips = ""
        while flips[-3:] != rosen and flips[-3:] != student:
            flips += random.choice(outcomes)
        winner = flips[-3:]
        if winner not in results:
            results[winner] = 1
        else:
            results[winner] += 1
    for key in results.keys():
        print(key,results[key]/1000)

headTails()
