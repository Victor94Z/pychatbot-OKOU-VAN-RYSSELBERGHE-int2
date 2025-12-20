from hogwart.universe.house import update_house_points, assign_house


'''houses = {
    "Gryffindor": 0,
    "Slytherin": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0
}
'''



def start_chapter_2(character, houses):
    character["House"] = assign_house(character, [
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
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends",
             "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ])

    houses = update_house_points(houses, character["House"], 100)
    print(input("Press enter to continue..."))
    return houses