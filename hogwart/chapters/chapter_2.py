import time

from hogwart.utils.input_utils import slow_print, load_file, build_file_path
from hogwart.universe.house import assign_house
from hogwart.universe.character import display_player

# Paths to data files
HOUSES_DATA_PATH = build_file_path("houses.json")

# Load data
houses = load_file(HOUSES_DATA_PATH)

#Handles the Hogwarts Express sequence. The player meets several characters and their choices influence their attributes.
def meet_friend(character):

    # Keeps track of attributes modified during this scene
    changed_attributes = []


    # Train introduction
    slow_print('{:^130}'.format(
        "You board the Hogwarts Express. The train slowly departs northward...\n"
    ))
    time.sleep(1)


    # Ron Weasley encounter
    slow_print('{:^130}'.format(
        "A red-haired boy enters your compartment, looking friendly.\n"
    ))

    answer_ron = {
        "1": "Sure, have a seat!",
        "2": "Sorry, I prefer to travel alone."
    }

    slow_print("— Hi! I'm Ron Weasley. Mind if I sit with you?\n")
    slow_print("How do you respond?\n")

    # Display possible answers
    for key in answer_ron:
        slow_print(f"{key}: {answer_ron[key]}")

    # Input validation loop
    while True:
        answer = input("\nYour choice: ")
        try:
            if 1 <= int(answer) <= len(answer_ron):
                break
            slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    # Apply consequences
    if int(answer) == 1:
        slow_print("\nRon smiles: — Awesome! You'll see, Hogwarts is amazing!\n")
        change = "Loyalty"
    else:
        slow_print("\nRon breaks down in tears: — NOOOOOOOOO WHYYYYYYYY!!")
        time.sleep(1)
        slow_print("...")
        time.sleep(2)
        slow_print("He evaporates into thin air as you reflect on your choice...\n")
        change = "Ambition"

    character["Attributes"][change] += 1
    if change not in changed_attributes:
        changed_attributes.append(change)

    time.sleep(1)


    # Hermione Granger encounter
    slow_print('{:^130}'.format(
        "A girl enters next, already carrying a stack of books.\n"
    ))

    answer_hermione = {
        "1": "Yes, I love learning new things!",
        "2": "Uh… no, I prefer adventures over books."
    }

    slow_print(
        "— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?\n\n"
        "How do you respond?\n"
    )

    for key in answer_hermione:
        slow_print(f"{key}: {answer_hermione[key]}")

    while True:
        answer = input("\nYour choice: ")
        try:
            if 1 <= int(answer) <= len(answer_hermione):
                break
            slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    if int(answer) == 1:
        slow_print("\nHermione smiles, impressed: — Oh, that's rare! You must be very clever!\n")
        change = "Intelligence"
    else:
        slow_print("\nHermione sighs: — I thought you would have been different...\n")
        slow_print("You're finally not special at all.\n")
        change = "Courage"

    character["Attributes"][change] += 1
    if change not in changed_attributes:
        changed_attributes.append(change)

    time.sleep(1)


    # Draco Malfoy encounter
    slow_print('{:^130}'.format(
        "Then a blonde boy enters, looking arrogant.\n"
    ))

    answer_draco = {
        "1": "Shake his hand politely.",
        "2": "Ignore him completely.",
        "3": "Respond with arrogance."
    }

    slow_print(
        "— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?\n\n"
        "How do you respond?\n"
    )

    for key in answer_draco:
        slow_print(f"{key}: {answer_draco[key]}")

    while True:
        answer = input("\nYour choice: ")
        try:
            if 1 <= int(answer) <= len(answer_draco):
                break
            slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    if int(answer) == 1:
        slow_print("\nDraco smirks: — Good boy.")
        change = "Ambition"
    elif int(answer) == 2:
        slow_print("\nDraco frowns, annoyed: — You'll regret that!")
        change = "Loyalty"
    else:
        slow_print(
            "\nDraco attempts a backflip, crashes through a window, and disappears into the night, screaming curses...\n"
        )
        time.sleep(1)
        change = "Courage"

    character["Attributes"][change] += 1
    if change not in changed_attributes:
        changed_attributes.append(change)

    # End of the train scene
    slow_print('{:^130}'.format(
        "The train continues its journey. Hogwarts Castle appears on the horizon...\n"
    ))

    slow_print("Your choices already reveal much about who you are.\nYour updated attributes:")
    for attr in changed_attributes:
        slow_print(f"{attr}: {character['Attributes'][attr]}")

    display_player(character)

#Displays Dumbledore-like welcome speech.
def welcome_message():

    print("\n * As you arrive at the school, a man with a long beard and a wizard's outfit is waiting for you at the gates. *\n ")
    intro = [
        "My dear students, it is with great joy that I welcome you on this most memorable day to Hogwarts, a sanctuary of magic and knowledge. \n"
        "You stand now at the threshold of an extraordinary journey — one that will carry you far beyond the boundaries of what you believe you know.",

        "Never forget that the truest magic does not lie solely in the spells you cast, nor in the potions you brew, but in the choices you make.\n "
        "Each failure will become a lesson, and each success a stone laid upon the foundation of your character.",

        "Hogwarts is more than a school; it is a family — a home where friendship is forged and differences are celebrated.",

        "So walk forward with confidence. Listen to the quiet voice of your conscience. \n",
        "May this year at Hogwarts be the one in which you discover the magic within yourselves."
    ]
    #Press Enter to read paragraph
    for paragraph in intro:
        slow_print(paragraph)
        input("\nPress Enter to continue...\n")

#Assigns the player to a house based on their attributes.
def sorting_ceremony(character):

    slow_print("\nProfessor Dumbledore’s voice echoes through the hall, inviting you to step inside the Great Hall.")
    slow_print("\nAs you take your place among the other students, the atmosphere grows quiet and expectant.")
    slow_print("\nAt the center of the room awaits the Sorting Hat, ready to determine where you belong.")
    slow_print("\nThe Sorting Ceremony is about to begin.")
    slow_print("\nIt's your turn, answer the questions that will determine your house.\n")

    # Questions to assign house
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
    house=character["House"]
    slow_print(
        f"You join the {house} students to loud cheers!"
    )

#Displays the player's common room introduction.
def enter_common_room(character):

    player_house = character["House"]
    slow_print(
        f"\nYou follow the prefects through the castle corridors...\n\n"
        f"{houses[player_house]['emoji']} {houses[player_house]['description']}\n"
        f"{houses[player_house]['installation_message']}\n"
    )

    # Display the colors of the player house
    colors = ", ".join(houses[player_house]["colors"])
    slow_print(f"Your colors are: {colors}")

# Start chapter 2 of the game
def start_chapter_2(character,houses):

    meet_friend(character)
    time.sleep(1)

    welcome_message()
    time.sleep(1)

    sorting_ceremony(character)
    time.sleep(1)

    print("\nThe entrance ceremony is now over; it is time for the students to go to their dormitories.\n")
    enter_common_room(character)
    time.sleep(1)

    print()
    display_player(character)
    print()
    # Chapter closing cinematic text
    slow_print(
        "Thus the chapter draws to a close, not with an ending, but with a pause — "
        "the kind that lingers like the final note of a spell well cast.\n"
        "The castle settles, torches bow to the night, and the echoes of discovery fade.\n"
        "And now… the hour turns.\n"
        "Classes begin, and with them, the first sparks of greatness.\n"
    )

    print(input("\nPress enter to continue...\n"))
    return houses







