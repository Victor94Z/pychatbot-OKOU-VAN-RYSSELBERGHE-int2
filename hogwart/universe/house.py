
from hogwart.utils.input_utils import ask_choice, slow_print
from hogwart.chapters.chapter_1 import create_character

def  update_house_points(houses, house_name, points):

    if house_name in houses:
        if points < 0 :
            slow_print(f"\n {house_name} loses {abs(points)} points ")
        else:
            slow_print(f"\n {house_name} wins {abs(points)} points ")
        houses[house_name] += points
        slow_print("\n The points are now : ",houses)
    else:
        slow_print("\n Warning, this house does not exist ! \n")
        need_remainder = ask_choice("Did you want a reminder of the existing houses ?",["Yes","No"])
        if need_remainder.lower() == "yes" or need_remainder.lower() == "1":
            slow_print("\n At Hogwarts, there are 4 main houses : Hufflepuff, Ravenclaw, Slytherin and Gryffindor")
        else:
            slow_print("\n Enter a valid house : ")


def display_winning_house(houses):
    max_points = None
    for score in houses.values():
        if max_points is None or score > max_points:
            max_points = score

    winning_house = []
    for key, value in houses.items():
        if value == max_points:
            winning_house.append(key)

    if len(winning_house) == 1:
        print()
        print(f"The house with the most points is {winning_house[0]} with {max_points} points.")

    elif len(winning_house) == 4:
        print()
        print(f"All houses are tied with {max_points} points.")
    else:
        print()
        print(f"Houses {", ".join(winning_house)} are tied with {max_points} points each.")

def assign_house(character,questions):
    houses = {
    "Gryffindor": 0,
    "Slytherin": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0
    }
    
    for i in range(len(questions)):
        question, answers, answer_houses = questions[i]

        slow_print(question)
        for j in range(len(answers)):
            slow_print(f"{j + 1} :  {answers[j]}")

        ans = int(input("\n What is your answer ? : "))
        print()

        chosen_house = answer_houses[ans - 1]
        houses[chosen_house] += 1

    houses["Gryffindor"] += character["Attributes"]["Courage"] * 2
    houses["Slytherin"] += character["Attributes"]["Ambition"] * 2
    houses["Hufflepuff"] += character["Attributes"]["Loyalty"] * 2
    houses["Ravenclaw"] += character["Attributes"]["Intelligence"] * 2

    winner = max(houses, key=houses.get)
    return winner

questions = [
    (
        "You see a friend in danger. What do you do?",
        ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),

    (
        "Which trait describes you best?",
        ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    ),

    (
        "When faced with a difficult challenge, you...",
        ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
        ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    )
]



