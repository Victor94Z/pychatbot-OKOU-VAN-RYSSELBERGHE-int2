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


