import time
import os
from hogwart.chapters.chapter_1 import create_character
from hogwart.utils.input_utils import slow_print, load_file
from hogwart.universe.house import assign_house
from hogwart.universe.character import BASE_DIR, display_player

HOUSES_DATA_PATH = os.path.join(BASE_DIR, "data", "houses.json")
houses = load_file(HOUSES_DATA_PATH)

player = create_character()

def meet_friend(character):

    changed_attributes = []

    slow_print('{:^130}'.format("You board the Hogwarts Express. The train slowly departs northward... \n"))#train introduction
    time.sleep(1)


    slow_print('{:^130}'.format("A red-haired boy enters your compartment, looking friendly. \n"))

    answer_ron = {"1" : "Sure, have a seat !","2" : "Sorry, i prefer to travel alone."}#ron possible responses
    slow_print("—Hi! I'm Ron Weasley. Mind if I sit with you ? \n")
    slow_print("How do you respond ? : \n")

    for i in answer_ron:#print the resposnses
        slow_print(f'{i}: {answer_ron[i]}')

    answer = "0"  
    while True:
        answer = input("\nYour choice: ")
        try:
            answer_int = int(answer)
            if 1 <= answer_int <= len(answer_ron):
                break  
            else:
                slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    if int(answer) == 1 :
        slow_print("\n Ron smiles: — Awesome! You'll see, Hogwarts is amazing! \n")
        change = "Loyalty"
        character["Attributes"][change] += 1
        if not change in changed_attributes:#change the attributes from the response
            changed_attributes.append(change)
    elif int(answer) == 2 :
        slow_print("\n Ron break down in tears: - NOOOOOOOOO WHHYYYYYYYYYY !!!!!!! ")
        time.sleep(1)
        slow_print("...")
        time.sleep(2)
        slow_print("he evaporates in the air as you think of what you did...\n")
        change = "Ambition"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    time.sleep(1)
    slow_print('{:^130}'.format("A girl enters next, already carrying a stack of books. \n"))




    answer_hermione = {"1" : "Yes, I love learning new things!","2" : "Uh… no, I prefer adventures over books."}#hermione possible resposnses
    slow_print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic' ? \n"
            "\n"
            "How do you respond ? : \n")
    
    for i in answer_hermione:
        slow_print(f'{i}: {answer_hermione[i]}')
        
    answer = "0"  
    while True:
        answer = input("\nYour choice: ")
        try:
            answer_int = int(answer)
            if 1 <= answer_int <= len(answer_hermione):
                break  
            else:
                slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    if int(answer) == 1 :
        slow_print("\n Hermione smiles, impressed: — Oh, that's rare! You must be very clever ! \n")
        change = "Intelligence"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif int(answer) == 2 :
        slow_print("\n Hermione looks at you in a disappointed way: -I thought you would have been different from the others...\n")
        slow_print("You're finally not special at all. \n")
        #insert video de moi qui cracvhe sur victor
        change = "Courage"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    
    time.sleep(1)
    slow_print('{:^130}'.format("Then a blonde boy enters, looking arrogant. \n"))




    answer_draco = {"1" : "Shake his hand politely.","2" : "Ignore him completely.","3" : "Respond with arrogance."}#draco possible responses
    slow_print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think ? \n"
          "\n"
          "How do you respond ? : \n")
    
    for i in answer_draco:
        slow_print(f'{i}: {answer_draco[i]}')

    answer = "0"  
    while True:
        answer = input("\n Your choice: ")
        try:
            answer_int = int(answer)
            if 1 <= answer_int <= len(answer_draco):
                break  
            else:
                slow_print("This is not a valid choice\n")
        except ValueError:
            slow_print("Please enter a valid integer\n")

    if int(answer) == 1 :
        slow_print("\n Draco is trying not to laugh: -Good boy.")
        change = "Ambition"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif int(answer) == 2 :
        slow_print("\n Draco frowns, annoyed. — You'll regret that!")
        change = "Loyalty"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif int(answer) == 3 :
        slow_print("\n Draco does a backflip and brake the glasse behind him, as he's flying out of the train he's cursing you:\n"
        " -YYOoOOuUUuuU MmAAaaADddDEeeE TTtHHHhIIiSssS HHhAAapPPEeeEnNNDD !!!! \n ...")
        time.sleep(1)
        change = "Courage"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    slow_print('{:^130}'.format("The train continues its journey. Hogwarts Castle appears on the horizon...\n"))

    slow_print("Your choices already say a lot about your personality! \n"
            "Your updated attributes: ")
    for i in changed_attributes:
        slow_print(f'{i} : {character["Attributes"][i]}')

def welcome_message():
    intro = [
    "My dear students, it is with great joy that I welcome you on this most memorable day to Hogwarts, a sanctuary of magic and knowledge."
    "You stand now at the threshold of an extraordinary journey — one that will carry you far beyond the boundaries of what you believe you know." 
    "Within these ancient walls, time-honoured traditions walk hand in hand with endless discovery."
    "Here, magic will reveal itself to you not as a force to be wielded without thought, but as a delicate art, demanding patience, wisdom, and a true heart." ,

    "Never forget that the truest magic does not lie solely in the spells you cast, nor in the potions you brew, but in the choices you make."
    "Courage in the face of adversity, loyalty to those who stand beside you, and the unyielding curiosity that drives you to learn and to understand "
    "— these are the powers that will shape your destiny. Each failure will become a lesson, and each success a stone laid upon the foundation of your character.",

    "Hogwarts is more than a school; it is a family — a home where friendship is forged, where differences are celebrated, and where tolerance and respect form the unseen pillars of our community."
    "Here, you will learn not only to excel on your own, but to stand together, to support one another in moments of darkness, and to share the light when it shines.",

    "So walk forward with confidence. Wear the colours of your house with pride, but above all, listen to the quiet voice of your conscience."
    "It will guide your steps when the path grows uncertain. The future before you is a blank page, waiting to be written by your actions and your wisdom."
    "May this year at Hogwarts be the one in which you discover not only the magic of the world around you, but the magic that resides within yourselves."
]

    for paragraph in intro:
        slow_print(paragraph)
        input("\n Press Enter to continue... \n")

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

def sorting_ceremony(character):
    house =  assign_house(character,questions)
    character["House"] = house
    slow_print(f"The Sorting Hat exclaims: {house} !\n You join the {house} students to loud cheers !")

def enter_common_room(character):
    player_house = character["House"]
    slow_print(f"""You follow the prefects through the castle corridors...\n 
    {houses[player_house]["emoji"]} {houses[player_house]["description"]} \n 
    {houses[player_house]["installation_message"]}\n""")
    colors = ", ".join(houses[player_house]["colors"])
    slow_print(f"Your colors are : {colors}")

def start_chapter_2(character):
    meet_friend(character)
    time.sleep(1)
    welcome_message()
    time.sleep(1)
    sorting_ceremony(character)
    time.sleep(1)
    enter_common_room(character)
    time.sleep(1)
    display_player(character)
    slow_print("Thus the chapter draws to a close, not with an ending, but with a pause — the kind that lingers in the air like the final note of a spell well cast. \n" \
    "The castle settles, torches bow to the night, and the echoes of discovery fade into the ancient stone. What has been learned is now yours to carry, for wisdom, once awakened, never truly sleeps.\n"
    "And now… the hour turns.\n"
    "The bells of Hogwarts toll softly, summoning minds and hearts alike. Corridors stir, doors creak open, and classrooms await their stories yet untold. Step forward with resolve, steady your hand and sharpen your intent — for classes begin, and within them lie the first sparks of greatness.\n")
    
start_chapter_2(player)