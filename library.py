import random
coin=random.choice (["Heads", "Tails"])
print (coin)

number= random.randint(1, 10)
print (number)

cards= ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print (card)


import statistics
print (statistics.mean([1, 2, 3, 4, 5]))

