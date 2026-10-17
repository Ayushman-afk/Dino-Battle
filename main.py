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
userChoice = int(input("Enter what Dinosaur you would like to fight with - \n 1. Trex\n 2. Stego\n 3. Triceratops\n Choice - "))
if userChoice == 1:
    userDino_name = "tRex"
    userDino_stats = tRex
    print("You Chose: ", userDino_name)
    print("Your Dinosaur Stats: ", userDino_stats)
elif userChoice == 2:
    userDino_name = "Stego"
    userDino_stats = Stego
    print("You Chose: ", userDino_name)
    print("Your Dinosaur Stats: ", userDino_stats)
elif userChoice == 3:
    userDino_name = "Triceratops"
    userDino_stats = Triceratops
    print("You Chose: ", userDino_name)
    print("Your Dinosaur Stats: ", userDino_stats)
else:
    userDino_name = tRex #defualt
    userDino_stats = tRex
    print("You Chose: ", userDino_name)
    print("Your Dinosaur Stats: ", userDino_stats)

compChoice = random.randint(1,3)
if compChoice == 1:
    compDino_name = "tRex"
    compDino_stats = tRex
elif compChoice == 2:
    compDino_name = "Stego"
    compDino_stats = Stego
elif compChoice == 3:
    compDino_name = "Triceratops"
    compDino_stats = Triceratops

print("Computer Chose: ", compDino_name)
print("Computer Dino Stats: ", compDino_stats)


# main Game loop

while compDino_stats["health"] > 0 and userDino_stats["health"] > 0:
    userStance = int(input("\n Enter your move - \n 1. Agressive\n 2. Defensive -  "))
    compStance = random.randint(1,2)

    if userStance == 1:
        userAttack = userDino_stats["attackA"]
        userDefense = userDino_stats["defenseA"]
    else:
        userAttack = userDino_stats["attackD"]
        userDefense = userDino_stats["defenseD"]

    if compStance == 1:
        compAttack = compDino_stats["attackA"]
        compDefense = compDino_stats["defenseA"]
    else:
        compAttack = compDino_stats["attackD"]
        compDefense = compDino_stats["defenseD"]

    compHPChange = max(0,userAttack - compDefense)
    userHPChange = max(0,compAttack - userDefense)


    compDino_stats["health"] -= compHPChange
    print("Computer HP: ", compDino_stats["health"])
    if compDino_stats["health"] <= 0:
        break

    userDino_stats["health"] -= userHPChange
    print("Your HP: ", userDino_stats["health"])
    if userDino_stats["health"] <= 0:
        break


if userDino_stats["health"] > 0:
    print("You WIN!!")
else:
    print("You LOSE!")





