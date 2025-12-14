import time
from hogwart.utils.input_utils import ask_number,ask_choice,ask_text
from hogwart.universe.character import init_character,display_player

#introduces the player at the beginning of the story
def introduction():
    print(input("Press Enter to begin the game..."))
    print()
    print('{:^130}'.format("Welcome to a world where magic is real…"))
    print()
    time.sleep(2)
    print('{:^130}'.format("For as long as you can remember, you have felt different."))
    time.sleep(2)
    print('{:^130}'.format(" Strange and unexplainable events have always seemed to happen around you, leaving you with more questions than answers."))
    print()
    print(input("Press Enter to continue..."))
    print('{:^130}'.format("Today marks the beginning of a new chapter in your life."))
    time.sleep(2)
    print('{:^130}'.format("You stand on the edge of something unknown, something extraordinary, even if you do not fully understand it yet."))
    print()
    print(input("Press Enter to continue..."))
    print('{:^130}'.format("An incredible journey awaits you — a journey filled with discoveries, challenges, and wonders beyond imagination."))
    time.sleep(3)
    print('{:^130}'.format("Your story begins now."))
    print()
    print(input("Press Enter to continue..."))
    print()


def  create_character():
    max_points = 20
    attributes={}

    last_name=ask_text("Enter your character's last name : ")
    first_name=ask_text("Enter your character's first name : ")

    print()
    print("Choose your attributes : ")
    print(f"You have {max_points} points to allocate among 4 skills ( Courage, Intelligence, Loyalty and Ambition ), choose wisely :")


    different_attribute = ["Courage", "Intelligence", "Loyalty", "Ambition"]

    end="False"
    while end == "False":
        max_points = 20
        points_used = 0
        remaining_points = max_points - points_used
        for attribute in different_attribute:
            print()
            print("Remaining points : ", remaining_points)

            if remaining_points == 0 and attribute in ["Loyalty", "Ambition"]:
                attributes[attribute] = 0
                print(f"{attribute} level (1-10) : 0")
                continue

            answer=ask_number(f"{attribute} level (1-10) : ",1,10)

            if answer > remaining_points:
                print("You do not have enough points remaining.")
                answer=ask_number(f"{attribute} level (1-10) : ",1,10)



            attributes[attribute]=answer
            points_used += answer

            remaining_points = max_points - points_used

        if remaining_points > 0:
            print()
            print(f"You still have {remaining_points} points to assign")
            add_remaining_point=ask_choice("Do you want to add the remaining points or lose them forever ?", ["Yes", "No"])
            if add_remaining_point.lower() == "no" or add_remaining_point.lower() == "2":
                end="True"
            else:
                print("Please start again")

        elif remaining_points == 0:
            print()
            validation=ask_choice("Do you want to confirm your choices ?",["Yes", "No"])
            if validation.lower() == "yes" or validation.lower() == "1":
                end="True"
            else:
                print("Please start again")


    character= init_character(last_name,first_name,attributes)


    print()
    print("Character profile:")
    print()
    print(f"Last name: {character['Last Name']}")
    print(f"First name: {character['First Name']}")
    print(f"Money: {character['Money']}")
    print("Inventory:")
    print("Spells:")
    print("Attributes:")
    for attr, value in character["Attributes"].items():
        print(f"- {attr}: {value}")
    print()
    print(input("Press Enter to continue..."))





def receive_letter():
    print()

    print(('{:^130}'.format("Night falls quietly around you.")))
    time.sleep(1.3)
    print('{:^130}'.format("The world seems calm… almost too calm."))
    time.sleep(2)
    print('{:^130}'.format("Suddenly, the sound of wings cuts through the silence."))
    print()
    print(input("Press Enter to continue..."))
    print('{:^130}'.format("The creature observes you for a moment before extending its leg."))
    time.sleep(2)
    print(('{:^130}'.format("Attached to it is an old parchment, carefully rolled and sealed with red wax bearing the Hogwarts crest.")))
    print()
    print(input("Press Enter to continue..."))
    print(('{:^130}'.format("Moments later, the owl takes flight and disappears into the darkness, leaving the letter behind.")))
    time.sleep(2)
    print(('{:^130}'.format("Curious and slightly nervous, you pick it up and gently break the seal.")))
    print()
    print(input("Press Enter to read the letter..."))
    print()
    print(('{:^130}'.format("---------------------------------------------------------------------------")))
    print()
    print("Dear Student,")
    print()
    time.sleep(1.2)
    print("We are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry!” ")
    print()
    time.sleep(1.2)
    accept_invitation=ask_choice("Do you accept this invitation and go to Hogwarts?", ["Yes, of course! ", "No, I'd rather stay with Uncle Vernon..."])
    if accept_invitation.lower() == "yes, of course!" or accept_invitation.lower() == "1":
        print()
        print("Congratulations,you have been accepted to Hogwarts!")
    else:
        print()
        print("You tear up the letter, and Uncle Vernon cheers :","\n","\n","EXCELLENT! Finally, someone NORMAL in this house!")
        print()
        print("The magical world will never know you existed...")
        print()
        time.sleep(1.2)
        print(('{:^130}'.format("GAME OVER")))
        exit()


