import json
import random


with open("hogwart/data/houses.json","r",encoding="utf-8") as h:
        house = json.load(h)

with open("hogwart/data./inventory.json","r") as f:
        inventory = json.load(f)



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


def init_character(first_name,last_name):

    house_name,house_attributes = random.choice(list(house.items())) 

    return {
        "last_name" : last_name,
        "first_name" : first_name,
        "money" : 100,
        "spells" : [],
        "inventory" : [],
        "house_attributes" : house_name,
        "courage" : random.randint(0,10), 
        "intelligence" : random.randint(0,10),
        "loyalty" : random.randint(0,10),
        "ambition" : random.randint(0,10)
    }


def display_player(player):

    print("\n",
          "First name : ",player["first_name"],"\n",
          "Laste name : ",player["last_name"],"\n",
          "Money : ",player["money"],"\n",
          "Spells : ",",".join(player["spells"]),"\n",
          "Inventory : ", ",".join(player["inventory"]),"\n",
          "House : ",player["house_attributes"]
          )
    
def modify_money(character,amount):

    character["money"] += amount
    return character["money"]

