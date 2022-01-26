from random import randint

cardColors = ['harten','klaveren','schoppen','ruiten']
cards = ['2','3','4','5','6','7','8','9','10','boer', 'vrouw','heer','aas']
joker = ['joker', 'joker']
game = list()
results = list()
for x in range(0,3):
    for y in range(0,12): game.append(cardColors[x] + " " + cards[y])
for z in range(0,1):
    game.append(joker[z])
for i in range(0, len(game)):
    results.append(game[randint(0, len(game)-1)])
for e in range(0,7):
    print(results[0])
    results.pop(0)
print(results)