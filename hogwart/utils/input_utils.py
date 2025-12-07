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


