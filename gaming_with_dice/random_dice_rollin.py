import random
import argparse
# I don't know any dice games with more than 6 dice used, so I stopped it at 6 dice.
parser = argparse.ArgumentParser(description='simulated 6 sided dice for a tons of games.')
parser.add_argument('--dice', type=int, required=True, help='number of dice for playing various games')
args = parser.parse_args()
num_of_die = args.dice


def roller_dice():
    if num_of_die == 1:
        dice_1 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
    elif num_of_die == 2:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
        print("Second die: %s" % dice_2)
    elif num_of_die == 3:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
        print("Second die: %s" % dice_2)
        print("Third die: %s" % dice_3)
    elif num_of_die == 4:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        dice_4 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
        print("Second die: %s" % dice_2)
        print("Third die: %s" % dice_3)
        print("fourth die: %s" % dice_4)
    elif num_of_die == 5:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        dice_4 = random.randint(1, 6)
        dice_5 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
        print("Second die: %s" % dice_2)
        print("Third die: %s" % dice_3)
        print("fourth die: %s" % dice_4)
        print("Fifth die: %s" % dice_5)
    elif num_of_die == 6:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        dice_4 = random.randint(1, 6)
        dice_5 = random.randint(1, 6)
        dice_6 = random.randint(1, 6)
        print("..Rolling..Dice..")
        print("First die: %s" % dice_1)
        print("Second die: %s" % dice_2)
        print("Third die: %s" % dice_3)
        print("fourth die: %s" % dice_4)
        print("Fifth die: %s" % dice_5)
        print("Sixth die: %s" % dice_6)
    else:
        print("Not a valid entry, 1-6 die")


roller_dice()
