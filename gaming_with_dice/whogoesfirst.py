import random
import argparse

parser = argparse.ArgumentParser(description='determine what player goes first randomly')
parser.add_argument('--players', type=int, required=True, help='number of players preparing to play')
args = parser.parse_args()
number_of_players = args.players


"""How do you decide who goes first in a game? Any game?
This script will tell you based on the number of players what order they should go in.

"""


def player_decider():
    player_dict = {}
    player_list = []
    if number_of_players <= 1:
        print('Not enough players to continue.')

# this range (2, 11) is because minimum 2 players, max 10
    elif 2 <= number_of_players <= 10:
        numb_player = number_of_players + 1
        listing_range = range(1, numb_player)

        for i in listing_range:
            user_input = input("Please provide character name: ")
            player_list.append(user_input)

        print(f"The player list is: {player_list}")
        for i in listing_range:
            randomness = random.choice(player_list)

            player_list.remove(randomness)
            player_dict['player_%s' % i] = randomness
        print(player_dict)

    else:
        print("input wasn't valid")


player_decider()
