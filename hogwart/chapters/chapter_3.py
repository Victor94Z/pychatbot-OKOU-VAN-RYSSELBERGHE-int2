import random
import time
from hogwart.universe.house import update_house_points, display_winning_house
from hogwart.utils.input_utils import load_file, build_file_path, slow_print
from hogwart.universe.character import display_player


# Path to spells data file
SPELLS_DATA_PATH = build_file_path("spells.json")

# Load spells data
spells = load_file(SPELLS_DATA_PATH)


# Allows the character to learn spells
def learn_spells(character, file_path="../data/spells.json"):
    print()
    print('{:^130}'.format("You begin your magic lessons at Hogwarts..."))
    print()
    print(input("Press Enter to start the lessons..."))

    # Maximum number of spells per category
    quotas = {
        "Offensive": 1,
        "Defensive": 1,
        "Utility": 3
    }

    spells_learn = []
    while quotas["Offensive"] > 0 or quotas["Defensive"] > 0 or quotas["Utility"] > 0: # Continue as long as there is at least one spell to learn

        # Pick a random spell
        spell = random.choice(spells)

        # Avoid learning the same spell twice
        if spell in spells_learn:
            continue

        spell_type = spell["type"]

        # Check if the spell type is still available
        if spell_type in quotas and quotas[spell_type] > 0:
            spells_learn.append(spell)
            character["Spells"].append(spell['name'])
            quotas[spell_type] -= 1

            print(f"You have just learned the spell: {spell["name"]} ({spell["type"]})")
            print(input("Press Enter to continue..."))

    # End of training
    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:\n")

    for spell_and_charc in range(len(spells_learn)):
        print(f"- {spells_learn[spell_and_charc]["name"]} ({spells_learn[spell_and_charc]["type"]}) : {spells_learn[spell_and_charc]["description"]}")


# Quiz to test magic knowledge
def magic_quiz(character, file_path="../data/magic_quiz.json"):
    print('{:^130}'.format("\nWelcome to the Hogwarts magic quiz!\n"))
    print("Answer the 4 questions correctly to earn points for your house.\n")

    # Load quiz questions
    questions = load_file(file_path)

    selected_questions = []
    score = 0

    # Select 4 random unique questions
    while len(selected_questions) < 4:
        question_rand = random.choice(questions)
        if question_rand not in selected_questions:
            selected_questions.append(question_rand)

    # Quiz
    for index in range(len(selected_questions)):
        print(f"{index + 1}. {selected_questions[index]['question']}")
        question = selected_questions[index]
        answer = input("> ").strip()

        # Check answer
        if answer.lower() == question["answer"].lower():
            print("Correct answer! +25 points for your house.\n")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {question['answer']}\n")

    # Display final score
    print(f"Score obtained: {score} points")

    return score

# Start chapter 3
def start_chapter_3(character,houses):
    # Learn spells
    learn_spells(character)
    print()
    print(input("Press Enter to continue..."))

    # Introduction to the quiz
    slow_print("\nBefore we continue, it’s time for a short magical test!")
    slow_print("This quiz will assess your knowledge of the wizarding world of Harry Potter.")
    slow_print("Each correct answer will earn points for your house, so stay focused and do your best!")

    # Launch quiz
    file_path=build_file_path("magic_quiz.json")
    score=magic_quiz(character, file_path)

    # Update house points
    houses=update_house_points(houses, character["House"], score)
    print()
    print(input("Press Enter to continue..."))
    print()

    # Display house rankings
    display_winning_house(houses)
    print()
    print(input("Press Enter to continue..."))
    print()


    # Display character summary
    slow_print("Alright, before moving on, let’s take a moment to review your character.")
    print()
    display_player(character)



