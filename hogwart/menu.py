from hogwart.chapters.chapter_1 import start_chapter_1
from hogwart.chapters.chapter_2 import start_chapter_2
from hogwart.chapters.chapter_3 import start_chapter_3
from hogwart.utils.input_utils import ask_choice


def display_menu():
    print()
    answer=ask_choice("START THE GAME ?", ["Start Chapter 1 – Arrival in the magical world.", "Exit the game."])

    return answer

def launch_menu_choice():

    init_houses={"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    #Display main menu
    answer = display_menu()

    if answer.lower() == "1" or answer.lower() == "start chapter 1 – arrival in the magical world.":
        print()
        # Chapter 1
        character = start_chapter_1()

        #Chapter 2
        print()
        houses=start_chapter_2(character,init_houses)

        #Chapter 3
        print()
        start_chapter_3(character, houses)
    else:
        exit()

