from character import *

houses = {
 "Gryffindor": 0,
 "Slytherin": 0,
 "Hufflepuff": 0,
 "Ravenclaw": 0
}

questions = [
("You see a friend in danger. What do you do?",
["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

("Which trait describes you best?",
["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

("When faced with a difficult challenge, you...",
["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])
]

player = init_character("a","b")
display_player(player)


def assign_house(character):
    for i in range(len(questions)):
        question, answers, answer_houses = questions[i]

        print(question)
        for j in range(len(answers)):
            print(j + 1, ": ", answers[j])

        ans = int(input("Quelle est votre réponse : "))

        chosen_house = answer_houses[ans - 1]
        houses[chosen_house] += 1

    houses["Gryffindor"] += character["courage"] * 2
    houses["Slytherin"] += character["ambition"] * 2
    houses["Hufflepuff"] += character["loyalty"] * 2
    houses["Ravenclaw"] += character["intelligence"] * 2

    winner = max(houses, key=houses.get)
    print("Votre maison est :", winner)

assign_house(player)



# def update_house_points(house_name,points):

#     houses[house_name] = points
#     return houses

# def winning_house():
    
#     max_points = max(houses.values())
#     best = [team for team,points in houses.items() if points == max_points]
#     if len(best) == 1:
#         print("La meilleure equipe est ",best[0]," avec ",max_points," points.")
#     else :
#          print(f"Egalité entre les equipes : {", ".join(best)} avec {max_points} points.")