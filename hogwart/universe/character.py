
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


def init_character(last_name, first_name, attributes) :

    character_init = {
        "Last_Name" : last_name,
        "First_Name" : first_name,
        "Money" : 100,
        "Spells" : [],
        "Inventory" : [],
        "Attributes": attributes,
        "House" : []
    }

    return character_init


def display_player(player):

    print("\n",
          "First name : ",player["First_Name"],"\n",
          "Laste name : ",player["Last_Name"],"\n",
          "House : ",player["House"],"\n",
          "Money : ",player["Money"],"\n",
          "Spells : ",", ".join(player["Spells"]),"\n",
          "Inventory : ", ", ".join(player["Inventory"]),"\n",
          "Attributes : ","\n",
          "     courage : ",player["Attributes"]["Courage"],"\n",
          "     intelligence : ",player["Attributes"]["Intelligence"],"\n",
          "     loyalty : ",player["Attributes"]["Loyalty"],"\n",
          "     ambition : ",player["Attributes"]["Ambition"],"\n",
    )


def modify_money(character,amount):

    character["Money"] += amount
    print()
    if amount > 0 :
        print(f"You have won {amount} galleons !")
        print()
        print("Your money : ",character["Money"])
    else:
        print(f"You have lost {abs(amount)} galleons !")
        print()
        print("Your money : ",character["Money"])





def add_item (character, key, item):
    print(f"You found: : {item} ")
    print()
    answer =ask_choice(f"Do you want to add '{item}' to your inventory ?",["Yes","No"])

    if answer.lower() == "yes" or answer.lower() == "1":
        character[key].append(item)
        print()
        return f"You added {item} to your inventory !"

    else:
        print()
        return f"No items have been added to your inventory"

'''
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

item_choice()
'''








