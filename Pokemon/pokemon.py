import json
import requests
import time 
import pprint
base_url = "https://pokeapi.co/api/v2/pokemon/"


list_names = []
def gather_pokemon():
    r = requests.get(base_url)
    #pprint.pprint(r.json())

    #list_names = []
    print(type(r.json()['results']))
    for i in r.json()['results']:
        #print(type(i))
        for key in i.values():
            if "https://" not in key:
                list_names.append(key)
    

    print(list_names)


    #we need to get more pokemeon from the list
    while r.json()['next'] is not None or len(list_names) < r.json()['count']:
    #print(r.json()['next'])
        if r.json()['next'] is not None:
            time.sleep(1
            )
            next_url = r.json()['next']
            r = requests.get(next_url)
            for i in r.json()['results']:
                for key in i.values():
                    if "https://" not in key:
                        list_names.append(key)

                    print(list_names)
                    print(len(list_names))
                    if len(list_names) == r.json()['count']:
                        
                        break





def gather_data():
    starting_letter = input("What does the name of the pokemon start with? ")
    if len(starting_letter) > 1:
        print("You have entered more than one letter")
    elif type(starting_letter) is not str:
        print("Not a string)")
    
    else:
        
        upper_case_input = starting_letter.upper()
        res = [idx for idx in list_names if idx[0].lower() == upper_case_input.lower()]
        print(res)
        print("There are {} number of Pokemon that start with letter {}".format(len(res), upper_case_input))
        pick_a_pokemon = input("Did you want to pick a pokemon to gather more data on that specific one? ")
        for condensed_pokemon_list in res:

            if pick_a_pokemon in condensed_pokemon_list:
                print('found')
                #add py request for url to gather that specific pokemon
                r = requests.get(base_url + pick_a_pokemon)
                print(r.status_code)


                pprint.pprint(r.json())
                



gather_pokemon()
gather_data()












#gather_pokemon()




