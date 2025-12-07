def ask_text(question):
    answer = input(question)
    while len(answer) == 0 or answer.isspace():
        answer = input(question).strip()

    return answer

import json

with open("inventory.json","r") as f:
    inventory = json.load(f)


for items_id, (items_name,price) in inventory.items():
    nb_item = items_id
    print(items_id," : ",items_name)

item_chosed = []
choice = input("Quel objet voulez vous choisir : ").split(" ")
for i in choice :
    if i in inventory:
        item_name = inventory[i][0]
        item_chosed.append(item_name)
    else :
        print("L'objet",i," n'est pas disponible bahahaa")

print("Vous avez choisi : ",end=" ")
for j in item_chosed:
    print(j,end=", ")


#print(F"name : {inventory('name')}")

def ask_choice(question, choices_list):
    print(question)
    size_list = len(choices_list)
    values_and_index = []
    for i in range(size_list):
        print(f"{i + 1}. {choices_list[i]}")

        values_and_index.append((choices_list[i].lower()))
        values_and_index.append(str(i + 1).lower())

    print("Your choice:", end=" ")
    answer = input()

    while answer.lower() not in values_and_index:
        print("Your choice have to be in the list :", end=" ")
        answer = (input())

    return answer



# # def ask_text(question):
# #     answer = input(question)
# #     while len(answer) == 0 or answer.isspace():
# #         answer = input(question).strip()

# #     return answer

import json
import random
def item_choice():
    with open("hogwart/data/inventory.json","r") as f:
        inventory = json.load(f)


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



# # # def ask_number(a,b):
# # #     choice = -1
# # #     while choice < a or choice > b:
# # #         choice = int(input(f"Choose a number between {a} and {b} : "))
# # #     return choice 

# # # choice = ask_number(1,10)
# # # print(choice)

# # #print(F"name : {inventory('name')}")



def init_character(first_name,last_name):

    with open("hogwart/data/houses.json","r",encoding="utf-8") as h:
        house = json.load(h)
    house_name,house_attributes = random.choice(list(house.items())) 


    return {
        "last_name" : last_name,
        "first_name" : first_name,
        "money" : 100,
        "spells" : [],
        "inventory" : [],
        "house_attributes" : house_name
    }
player = init_character("prenom","nom")


def display_player(player):
    print("\n",
          "First name : ",player["first_name"],"\n",
          "Laste name : ",player["last_name"],"\n",
          "Money : ",player["money"],"\n",
          "Spells : ",",".join(player["spells"]),"\n",
          "Inventory : ", ",".join(player["inventory"]),"\n",
          "House : ",player["house_attributes"]
          )


new_inv = item_choice()
player["inventory"].extend(new_inv)
display_player(player)


