import time
from hogwart.chapters.chapter_1 import create_character
from hogwart.utils.input_utils import slow_print
player = create_character()

def meet_friend(character):

    changed_attributes = []

    slow_print('{:^130}'.format("You board the Hogwarts Express. The train slowly departs northward... \n"))#train introduction
    time.sleep(2)


    slow_print('{:^130}'.format("A red-haired boy enters your compartment, looking friendly. \n"))
    time.sleep(2)

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
        time.sleep(1)
        slow_print("he evaporates in the air as you think of what you did...\n")
        change = "Ambition"
        character["Attributes"][change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    slow_print('{:^130}'.format("A girl enters next, already carrying a stack of books. \n"))
    time.sleep(2)




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
    
    slow_print('{:^130}'.format("Then a blonde boy enters, looking arrogant. \n"))
    time.sleep(2)




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


meet_friend(player)