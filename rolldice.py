import random

response = "y"

while response == "y":
    roll = random.randint(1, 6)
    if roll == 1:
        print(" 
          _____
         |     |
         |  o  |
         |_____|")
    elif roll == 2:
        print(" 
          _____
         |o    |
         |     |
         |____o|")
    elif roll == 3:
        print(" 
          _____
         |o    |
         |  o  |
         |____o|")
    elif roll == 4:
        print(" 
          _____
         |o   o|
         |     |
         |o___o|")
    elif roll == 5:
        print(" 
          _____
         |o   o|
         |  o  |
         |o___o|")
    else:
        print(" 
          _____
         |o   o|
         |o   o|
         |o___o|")
    response = input("Roll again? (y/n)")
