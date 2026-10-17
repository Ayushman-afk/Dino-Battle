import random

tRex = {
    "health" : 20,
    "attackA": random.randint(6,10),
    "attackD": random.randint(4,8),
    "defenseA": random.randint(0,2),
    "defenseD": random.randint(3,5),
}

Stego = {
    "health" : 40,
    "attackA": random.randint(3,6),
    "attackD": random.randint(1,4),
    "defenseA": random.randint(1,3),
    "defenseD": random.randint(4,8),
}

Triceratops = {
    "health" : 30,
    "attackA": random.randint(4,8),
    "attackD": random.randint(2,6),
    "defenseA": random.randint(1,4),
    "defenseD": random.randint(2,6),
}
userChoice = int(input("Enter what Dinosaur you would like to fight with - /n 1. Trex\n 2. Stego\n 3. Triceratops\n Choice - "))
if userChoice == 1:
    userDino = tRex
elif userChoice == 2:
    userDino = Stego
elif userChoice == 3:
    userDino = Triceratops
else:
    userDino = tRex #defualt

compChoice = random.randint(1,3)
if compChoice == 1:
    compDino = tRex
elif compChoice == 2:
    compDino = Stego
else:
    compDino = Triceratops
