

from hogwart.utils.input_utils import ask_choice

def  update_house_points( houses, house_name, points):


    if house_name in houses:
        if points < 0 :
            print()
            print(f"{house_name} loses {abs(points)} points ")
        else:
            print()
            print(f"{house_name} wins {abs(points)} points ")
        houses[house_name] += points
        print()
        print(f"The points are now : {houses} ",end="")
        return houses

    else:
        print()
        print("Warning, this house does not exist !")
        print()
        need_remainder = ask_choice("Did you want a reminder of the existing houses ?",["Yes","No"])
        if need_remainder.lower() == "yes" or need_remainder.lower() == "1":
            print()
            print("At Hogwarts, there are 4 main houses : Hufflepuff, Ravenclaw, Slytherin and Gryffindor")

        print()
        valid_house=input("Enter a valid house : ")


        return update_house_points(houses, valid_house, points)




def display_winning_house(houses):
    print()
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
        print(f"The house with the most points is {winning_house[0]} with {max_points} points.\n")

    elif len(winning_house) == 4:
        print()
        print(f"All houses are tied with {max_points} points.\n")
    else:
        print()
        print(f"Houses {", ".join(winning_house)} are tied with {max_points} points each.\n")



def assign_house(character,questions):

    character_attributes = character['Attributes']

    score_houses={"Gryffindor": 0,"Slytherin": 0,"Hufflepuff":0,"Ravenclaw": 0}

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
                houses = questions[i][2][value-1]
                score_houses[houses] += 3
                break

    print()
    print("Summary of scores :")
    for key, value in score_houses.items():
        print(f"{key} : {value} points")


    max_score = max(score_houses.values())

    tied_houses = []
    for houses, score in score_houses.items():
        if score == max_score:
            tied_houses.append(houses)


    if len(tied_houses) == 1:
        print(f"\nCongratulations ! You have been sorted into {tied_houses[0]}!")
        return tied_houses[0]


    print("\nSeveral houses are tied! One final question to decide.\n")

    tie_question = "In one word, how do you usually react in an emergency?"
    tie_answers = {
        "Gryffindor": "Act immediately, without fear",
        "Slytherin": "Think ahead and choose the smartest move",
        "Hufflepuff": "Make sure everyone is safe and supported",
        "Ravenclaw": "Observe carefully before taking action"
    }

    tie_choices = []

    for houses in tied_houses:
        tie_choices.append(tie_answers[houses])


    tie_answer = ask_choice(tie_question, tie_choices)

    for i in range(len(tie_choices)):
        if tie_answer.lower() == tie_choices[i].lower() or tie_answer == str(i + 1):
            final_house = tied_houses[i]
            print(f"\nCongratulations ! You have been sorted into {final_house}!")
            print()
            return final_house

    return None



'''

def_character = init_character("OKOU","Victor",{"Courage":5,"Intelligence":5,"Loyalty":5,"Ambition":5})
house=update_house_points({"Gryffindor": 0,"Slytherin": 0,"Hufflepuff": 0,"Ravenclaw": 0},"Gryffindor",150)
print(house)
display_winning_house(house)

assign_house(def_character,[
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
])
'''