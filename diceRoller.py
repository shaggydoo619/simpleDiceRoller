import random

while True:
    try:
        rollConf = int(input("What dice you wanna roll?(print 0 for stop): "))
        if rollConf == 0:
          break
        dices = int(input("How many dices you wanna roll? "))
        sum = 0
        for _ in range (dices):
            sum += random.randint(1, rollConf)
        print(f"You rolled {sum} in {dices}d{rollConf}")
    except:
        print("Please input integer number")
        continue
print("See you later!")
input()