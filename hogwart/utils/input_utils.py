import json

def ask_text(question):
    answer = input(question)
    while len(answer) == 0 or answer.isspace():
        answer = input(question).strip()

    return answer


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


def load_file(address):
    with open(address,"r") as f:
        file = json.load(f)
        return file

def ask_number(a,b):
    choice = -1
    while choice < a or choice > b:
        choice = int(input(f"Choose a number between {a} and {b} : "))
    return choice 
