import time
import os


from hogwart.utils.input_utils import ask_text, ask_number, ask_choice, load_file
from hogwart.universe.character import init_character, display_player,BASE_DIR,modify_money



INVENTORY_DATA_PATH = os.path.join(BASE_DIR, "data", "inventory.json")
HOUSES_DATA_PATH = os.path.join(BASE_DIR, "data", "houses.json")

house = load_file(HOUSES_DATA_PATH)
inventory = load_file(INVENTORY_DATA_PATH)

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


def  create_character(max_points=24):
    remaining_points = max_points
    attributes={}

    last_name=ask_text("Enter your character's last name : ")
    first_name=ask_text("Enter your character's first name : ")

    print()
    print("Choose your attributes : ")
    print(f"You have {remaining_points} points to allocate among 4 skills ( Courage, Intelligence, Loyalty and Ambition ), choose wisely :")


    different_attribute = ["Courage", "Intelligence", "Loyalty", "Ambition"]

    end="False"
    while end == "False":
        remaining_points = max_points

        for attribute in different_attribute:
            print()
            print("Remaining points : ", remaining_points)

            if remaining_points == 0 :
                attributes[attribute] = 0
                print(f"{attribute} level (1-10) : 0")
                continue

            answer=ask_number(f"{attribute} level (1-10) : ",1,10)

            while answer > remaining_points:
                print("You do not have enough points remaining.")
                answer=ask_number(f"{attribute} level (1-10) : ",1,10)

            attributes[attribute]=answer
            remaining_points -= answer

        if remaining_points > 0:
            print()
            print(f"You still have {remaining_points} points to assign")
            add_remaining_point=ask_choice("Do you want to add the remaining points (if not , you will lose them forever ) ?", ["Yes", "No"])
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
    display_player(character)
    print()
    print(input("Press Enter to continue..."))

    return character



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
    print(('{:^130}'.format("---------------------------------------------------------------------------")))
    print()
    time.sleep(1.2)
    accept_invitation=ask_choice("Do you accept this invitation and go to Hogwarts?", ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])
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
    print()

def meet_hagrid(character):
    print("\n Suddenly, a loud crash echoes from the door. A giant figure stands there, but you have no idea who he is or what he wants.")
    print()
    time.sleep(2.5)
    print(f"You: ( * With a trembling voice * ) 'Uh… who are you?'")
    print()
    time.sleep(2.5)
    print(f"Stranger: 'Hello {character["First Name"]}! I'm Hagrid. Dumbledore, the headmaster of Hogwarts, sent me to guide you to the school.'")
    print()
    time.sleep(2.5)
    choice=ask_choice("Do you want to follow Hagrid ?", ["Yes", "No"])

    if choice.lower() == "yes" or choice.lower() == "1":
        print("Hagrid: 'Perfect! But before we head to Hogwarts, we need to do some shopping in Diagon Alley.'")
    else:
        print("* You hesitate, but Hagrid gently insists and takes you along anyway! *")
        print()
        time.sleep(2)
        print("Hagrid: 'No worries, but first we have to go shopping in Diagon Alley!'")

    print()
    time.sleep(2.5)
    print("* Together, you leave the house and head toward Diagon Alley, ready for magical adventures… *")


def buy_supplies(character):
    print(f"Welcome to Diagon Alley {character["First Name"]}! \n")


    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]
    buy_required = []

    # Display catalog
    print("Catalog of available items:\n")
    for key, (name, price) in inventory.items():
        required = " (required)" if name in required_items else ""
        print(f"{key}. {name} - {price} Galleons{required}")

    # Buy required items
    while len(buy_required) < len(required_items)  :
        print(f"\nYou have {character["Money"]} Galleons.")
        remaining = [item for item in required_items if item not in buy_required]
        print("Remaining required items:", ", ".join(remaining))

        #
        if len(remaining) > 0 and character["Money"]==0:
            print("You don't have enough money to buy all the requested items. You lose the game. You only had 3 items to buy, really, how do you manage your money ?!\n")
            print('{:^130}'.format("GAME OVER"))
            exit()

        choice = input("Enter the number of the item to buy: ").strip()

        while choice not in inventory:
            choice = input("Invalid choice. Enter a valid item number: ").strip()

        item_name, item_price = inventory[choice]

        buy_item=True
        if item_name not in required_items:
            print("\nThis item is not required right now.")
            buy_not_required=ask_choice("Are you really sure you want to buy this item? Be careful, this choice could have consequences for the rest of your adventure.",["Yes","No"])
            if buy_not_required.lower() in ["no","2"] :
                print("Purchase cancelled.")
                buy_item=False
            if buy_not_required.lower() in ["yes","1"] :
                if item_price> character["Money"]:
                    print("\nYou don't have enough money !\n")
                    continue


        if [item_name in remaining] and item_price > character["Money"] :
            print("You don't have enough money to buy all the requested items. You lose the game. You only had 3 items to buy, really, how do you manage your money ?!\n")
            print('{:^130}'.format("GAME OVER"))
            exit()



        if buy_item:
            modify_money(character,-item_price)
            character["Inventory"].append(item_name)
            if item_name in remaining:
                buy_required.append(item_name)

            print(f"\nYou bought: {item_name} (-{item_price} Galleons).")



    print(f"\nYou have {character["Money"]} Galleons.")
    print("\nAll required items have been purchased!")


def character_pet(character):

    # Pets
    pets = {
        "Owl": 20,
        "Cat": 15,
        "Rat": 10,
        "Toad": 5
    }

    print("\nIt's time to choose your Hogwarts pet!")
    print(f"\nYou have {character['Money']} Galleons.\n")
    print("Available pets:")

    pet_names = []
    pet_prices=[]
    counter = 1

    # Display pets
    for pet in pets:
        price = pets[pet]
        print(f"{counter}. {pet} - {price} Galleons")
        pet_names.append(pet)
        pet_prices.append(price)
        counter += 1

    min_price = min(pet_prices)



    if character["Money"] < min_price:
        print("You don't have enough money to buy any pet. You lose the game.")
        print('{:^130}'.format("GAME OVER"))
        exit()

    while True:
        choice = input("\nEnter the number of the pet you want: ").strip()

        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(pet_names):
            choice = input("Invalid choice. Enter a valid pet number: ").strip()

        pet = pet_names[int(choice) - 1]
        pet_price = pets[pet]


        if pet_price > character["Money"]:
            print("You don't have enough money for this pet. Try another one. ")
            continue


        modify_money(character,-pet_price)
        character["Inventory"].append(pet)

        print(f"\nYou chose: {pet} (-{pet_price} Galleons).\n")
        break

    display_player(character)

def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter()
    print(input("Press Enter to continue..."))
    meet_hagrid(character)
    print(input("\nPress Enter to continue..."))
    buy_supplies(character)
    print(input("\nPress Enter to continue..."))
    character_pet(character)
    print()
    print('{:^130}'.format("End of Chapter 1! You survived Diagon Alley without going bankrupt (well done). "))
    print()
    print('{:^130}'.format("Wand in hand, pet at your side,it’s time to face classes, mysteries, and questionable life choices. "))
    print()
    print('{:^130}'.format("Welcome to Hogwarts..."))




