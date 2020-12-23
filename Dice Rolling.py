import random

print("(0)Exit\n(1)Roll A Dice\n(2)Roll Two Dices")

while True:
    soru = input("Select: ")

    if soru == "0":
        print("See you later!")
        break

    elif soru == "1":
        print("Rolling the dice...")
        dice = random.randint(1,6)
        print(dice)

    elif soru == "2":
        print("Rolling dices...")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(dice1, dice2)

    else:
        print("Try again")
        print("(0)Exit\n(1)Roll A Dice\nRoll Two Dices")