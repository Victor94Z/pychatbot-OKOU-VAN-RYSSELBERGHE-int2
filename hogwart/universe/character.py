import json
import random
import os

from hogwart.utils.input_utils import ask_choice, load_file

# folder of THIS file (hogwart/universe)
CURRENT_DIR = os.path.dirname(__file__)

# go up one folder: hogwart/
BASE_DIR = os.path.dirname(CURRENT_DIR)

# build full path: hogwart/data/houses.json
INVENTORY_DATA_PATH = os.path.join(BASE_DIR, "data", "inventory.json")
HOUSES_DATA_PATH = os.path.join(BASE_DIR, "data", "houses.json")

house = load_file(HOUSES_DATA_PATH)
inventory = load_file(INVENTORY_DATA_PATH)


def item_choice():

    for items_id, (items_name,price) in inventory.items():
        nb_item = items_id
        print(items_id," : ",items_name)

    item_chosed = []
    choice = input("Quel objet voulez vous choisir : ").split(" ")
    for i in choice :
        if i == "0" :
            print("Vous n'avez rien choisi")
            return []
        if i in inventory:
            item_name = inventory[i][0]
            item_chosed.append(item_name)
        else :
            print("L'objet",i," n'est pas disponible bahahaa")

    print("Vous avez choisi : ",end=" ")
    for j in item_chosed:
        print(j,end=", ")

    return item_chosed


def init_character(last_name, first_name, attributes) :

    return {
        "Last Name" : last_name,
        "First Name" : first_name,
        "Money" : 100,
        "Spells" : [],
        "Inventory" : [],
        "Attributes": attributes,
    }


def display_player(player):

    print("\n",
          "First name : ",player["first_name"],"\n",
          "Laste name : ",player["last_name"],"\n",
          "Money : ",player["money"],"\n",
          "Spells : ",", ".join(player["spells"]),"\n",
          "Inventory : ", ", ".join(player["inventory"]),"\n",
          "Attributes : ","\n",
          "     courage : ",player["courage"],"\n",
          "     intelligence : ",player["intelligence"],"\n",
          "     loyalty : ",player["loyalty"],"\n",
          "     ambition : ",player["loyalty"],"\n",
          )
    
def modify_money(character,amount):

    character["money"] += amount
    return character["money"]





def add_item (character, key, item):
    print(f"You found: : {item} ")

    answer =ask_choice("Do you want to add the item to your inventory ?",["Yes","No"])

    if answer.lower() == "yes":
        character[key].extend([item])
        return f"You added {item} to your inventory !"
    elif answer.lower() == "no":
        return f"No items have been added to your inventory"


