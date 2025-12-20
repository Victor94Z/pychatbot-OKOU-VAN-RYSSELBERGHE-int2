import random
import time
from hogwart.universe.house import update_house_points, display_winning_house
from hogwart.utils.input_utils import load_file, build_file_path
from hogwart.universe.character import display_player


SPELLS_DATA_PATH = build_file_path("spells.json")
spells = load_file(SPELLS_DATA_PATH)



# CHAP 3 - "Classes and Discovering Hogwarts"


def learn_spells(character, file_path="../data/spells.json"):
    print()
    print('{:^130}'.format("You begin your magic lessons at Hogwarts..."))
    print()
    print(input("Press Enter to start the lessons..."))

    quotas = {
        "Offensive": 1,
        "Defensive": 1,
        "Utility": 3
    }

    spells_learn = []
    while sum(quotas.values()) > 0:

        spell = random.choice(spells)

        if spell in spells_learn:
            continue

        spell_type = spell["type"]


        if spell_type in quotas and quotas[spell_type] > 0:
            spells_learn.append(spell)
            character["Spells"].append(spell['name'])
            quotas[spell_type] -= 1
            print(f"You have just learned the spell: {spell["name"]} ({spell["type"]})")
            print(input("Press Enter to continue..."))


    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:\n")

    for spell_and_charc in range(len(spells_learn)):
        print(f"- {spells_learn[spell_and_charc]["name"]} ({spells_learn[spell_and_charc]["type"]}) : {spells_learn[spell_and_charc]["description"]}")



def magic_quiz(character, file_path="../data/magic_quiz.json"):
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.\n")

    questions = load_file(file_path)

    selected_questions = []
    score = 0

    while len(selected_questions) < 4:
        question_rand = random.choice(questions)
        if question_rand not in selected_questions:
            selected_questions.append(question_rand)



    # Quiz
    for index in range(len(selected_questions)):
        print(f"{index + 1}. {selected_questions[index]['question']}")
        question = selected_questions[index]
        answer = input("> ").strip()

        if answer.lower() == question["answer"].lower():
            print("Correct answer! +25 points for your house.\n")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {question['answer']}\n")


    print(f"Score obtained: {score} points")

    return score

def start_chapter_3(character,houses):
    learn_spells(character)
    print()
    print(input("Press Enter to continue..."))
    print("\nBefore we continue, it’s time for a short magical test!")
    time.sleep(2)
    print("This quiz will assess your knowledge of the wizarding world of Harry Potter.")
    time.sleep(2)
    print("Each correct answer will earn points for your house, so stay focused and do your best!")
    time.sleep(2)
    file_path=build_file_path("magic_quiz.json")
    score=magic_quiz(character, file_path)
    houses=update_house_points(houses, character["House"], score)
    print()
    print(input("Press Enter to continue..."))
    print()
    display_winning_house(houses)
    print()
    print(input("Press Enter to continue..."))
    print()
    print("Alright, before moving on, let’s take a moment to review your character.")
    print()
    display_player(character)



