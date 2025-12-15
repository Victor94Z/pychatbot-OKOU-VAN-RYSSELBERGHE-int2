from character import *
from hogwart.utils.input_utils import ask_choice

houses = {
 "Gryffindor": 0,
 "Slytherin": 0,
 "Hufflepuff": 0,
 "Ravenclaw": 0
}

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



def  update_house_points(houses, house_name, points):

    if house_name in houses:
        if points < 0 :
            print()
            print(f"{house_name} loses {abs(points)} points ")
        else:
            print()
            print(f"{house_name} wins {abs(points)} points ")
        houses[house_name] += points
        print()
        print("The points are now : ",houses)
    else:
        print()
        print("Warning, this house does not exist !")
        print()
        need_remainder = ask_choice("Did you want a reminder of the existing houses ?",["Yes","No"])
        if need_remainder.lower() == "yes" or need_remainder.lower() == "1":
            print()
            print("At Hogwarts, there are 4 main houses : Hufflepuff, Ravenclaw, Slytherin and Gryffindor")
        else:
            print()
            print("Enter a valid house : ")


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
    score_houses={"Gryffindor":0,"Slytherin":0,"Hufflepuff":0,"Ravenclaw":0}
    character_attributes = character["Attributes"]

    # Initialise houses points
    for key,value in character_attributes.items():
        if key == 'Courage' :
            score_houses["Gryffindor"] += value*2
        elif key == 'Ambition' :
            score_houses["Slytherin"] += value*2
        elif key == 'Loyalty' :
            score_houses["Hufflepuff"] += value*2
        elif key == 'Intelligence' :
            score_houses["Ravenclaw"] += value*2

    #Attribute points with questions
    print()
    for i in range(3):
        print()
        question_answer=ask_choice(questions[i][0],questions[i][1])
        for value in range(len(questions[i][1])+1):
            str_answer=questions[i][1][value-1]
            str_value=str(value)
            if question_answer.lower() == str_answer.lower() or question_answer == str_value :
                house = questions[i][2][value-1]
                score_houses[house] += 3
                break

    print()
    print("Summary of scores :")
    for key, value in score_houses.items():
        print(f"{key} : {value} points")




