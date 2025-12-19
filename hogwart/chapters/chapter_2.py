import random
import json

from hogwart.universe.house import update_house_points
from hogwart.utils.input_utils import ask_text, ask_number, ask_choice, load_file
from hogwart.universe.character import init_character, display_player,BASE_DIR,modify_money


# CHAP 2 - "Classes and Discovering Hogwarts"
def  learn_spells(character, file_path="../data/spells.json"):
    print("\nYou begin your magic lessons at Hogwarts...\n")

    with open(file_path) as json_file:
        spells = json.load(json_file)


    print(input("Press Enter to continue..."))


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
            character["Spells"].append(spell)
            quotas[spell_type] -= 1
            print(f"You have just learned the spell: {spell["name"]} ({spell["type"]})")
            print(input("Press Enter to continue..."))

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:\n")

    for spell in character["Spells"]:
        print(f"- {spell["name"]} ({spell["type"]}): {spell["description"]}")

'''
def  magic_quiz(character, file_path="../data/magic_quiz.json"):
    print("\nWelcome to the Hogwarts magic quiz! \nAnswer the 4 questions correctly to earn points for your house.")


    questions = load_file(magic_quiz)

    score = 0
    quiz_questions=[]
    
    while len(quiz_questions) < 4:
        question = random.choice()
        print(question)

        if question in quiz_questions['question']:
            continue

        quiz_questions.append(question)
'''






def magic_quiz(character, file_path="../data/magic_quiz.json"):
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.\n")

    questions = load_file(file_path)

    selected_questions = []
    score = 0

    # Tirer 4 questions uniques
    while len(selected_questions) < 4:
        q = random.choice(questions)
        if q not in selected_questions:
            selected_questions.append(q)

    # Quiz
    for i, q in enumerate(selected_questions, start=1):
        print(f"{i}. {q['question']}")
        answer = input("> ").strip()

        if answer.lower() == q["answer"].lower():
            print("Correct answer! +25 points for your house.\n")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {q['answer']}\n")

    # Résultat final
    print(f"Score obtained: {score} points")

    # Ajout au score du personnage
    update_house_points("")


character = init_character("OKOU","Victor",{"Courage":5})
magic_quiz(character)