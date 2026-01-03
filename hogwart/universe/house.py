from utils.input_utils import ask_choice

# Update the points of a given house
def  update_house_points( houses, house_name, points):

    # Check if the house exists
    if house_name in houses:
        print()

        # Display win or loss message
        if points < 0 :
            print(f"{house_name} loses {points} points ")
        else:
            print(f"{house_name} wins {points} points ")

        # Update the house points
        houses[house_name] += points
        print()
        print(f"The points are now : {houses} ",end="")
        return houses

    # If the house does not exist ( useful if at some point the user has to enter a house themselves )
    else:
        print()
        print("Warning, this house does not exist !")
        print()

        # Ask if the user wants a reminder of the houses
        need_remainder = ask_choice("Did you want a reminder of the existing houses ?",["Yes","No"])
        if need_remainder.lower() == "yes" or need_remainder.lower() == "1":
            print()
            print("At Hogwarts, there are 4 main houses : Hufflepuff, Ravenclaw, Slytherin and Gryffindor")

        print()

        # Ask again for a valid house
        valid_house=input("Enter a valid house : ")

        # Retry the function with the new input
        return update_house_points(houses, valid_house, points)


# Display the house(s) with the highest score
def display_winning_house(houses):
    print()

    # Find the maximum number of points
    max_points = None
    for score in houses.values():
        if max_points is None or score > max_points:
            max_points = score

    # Find all houses with the maximum score
    winning_house = []
    for key, value in houses.items():
        if value == max_points:
            winning_house.append(key)

    # Display result
    if len(winning_house) == 1:
        print()
        print(f"The house with the most points is {winning_house[0]} with {max_points} points.\n")

    elif len(winning_house) == 4:
        print()
        print(f"All houses are tied with {max_points} points.\n")
    else:
        print()
        print(f"Houses {", ".join(winning_house)} are tied with {max_points} points each.\n")


# Assign a house to a character
def assign_house(character,questions):

    # Get character attributes
    character_attributes = character['Attributes']

    # Initialize house scores
    score_houses={
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff":0,
        "Ravenclaw": 0
    }

    # Initialise houses points with attributes ( x2 )
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

    # Display score summary
    print()
    print("Summary of scores :")
    for key, value in score_houses.items():
        print(f"{key} : {value} points")

    # Find the maximum score
    max_score = max(score_houses.values())

    # Find houses with the same max score
    tied_houses = []
    for houses, score in score_houses.items():
        if score == max_score:
            tied_houses.append(houses)

    # If only one house wins
    if len(tied_houses) == 1:
        print(f"\nCongratulations ! The Sorting Hat exclaims: {tied_houses[0]}!")
        return tied_houses[0]

    # Tie-breaker question
    print("\nSeveral houses are tied! One final question to decide.\n")

    tie_question = "In one word, how do you usually react in an emergency?"
    tie_answers = {
        "Gryffindor": "Act immediately, without fear",
        "Slytherin": "Think ahead and choose the smartest move",
        "Hufflepuff": "Make sure everyone is safe and supported",
        "Ravenclaw": "Observe carefully before taking action"
    }

    tie_choices = []

    # Generate answers based on tied houses
    for houses in tied_houses:
        tie_choices.append(tie_answers[houses])

    # Determine final house
    tie_answer = ask_choice(tie_question, tie_choices)

    for i in range(len(tie_choices)):
        if tie_answer.lower() == tie_choices[i].lower() or tie_answer == str(i + 1):
            final_house = tied_houses[i]
            print(f"\nCongratulations ! The Sorting Hat exclaims: {final_house}!")
            print()
            return final_house

    # Safety return (should not happen)
    return None

