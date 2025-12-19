from chapter_1 import create_character
character = create_character("prenom","nom",["Courage", "Intelligence", "Loyalty", "Ambition"])

def meet_friend(character):

    changed_attributes = []

    print("You board the Hogwarts Express. The train slowly departs northward...")
    print("A red-haired boy enters your compartment, looking friendly.")

    answer_ron = {"1" : "Sure, have a seat !","2" : "Sorry, i prefer to travel alone."}
    print("—Hi! I'm Ron Weasley. Mind if I sit with you?" "\n"
          "How do you respond ? : ")
    for i in answer_ron:
        print(i)
    answer = 0
    while answer < 1 or answer > len(answer_ron):
        answer = input("Your choice : ")
        if answer < 1 or answer > len(answer_ron): 
            print("This is not  valid choice")
    print("Your choice : ",answer)
    if answer == 1 :
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        change = "Loyalty"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif answer == 2 :
        print("Ron break down in tears: - NOOOOOOOOO WHHYYYYYYYYYY !!!!!!!","\n",
              "...""\n",
              "he evaporates in the air as you think of what you did")
        change = "Ambition"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    print("A girl enters next, already carrying a stack of books.")

    answer_hermione = {"1" : "Yes, I love learning new things!","2" : "Uh… no, I prefer adventures over books."}
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?""\n"
            "How do you respond? : ")
    for i in answer_hermione:
        print(i)
    answer = 0
    while answer < 1 or answer > len(answer_hermione):
        answer = input("Your choice : ")
        if answer < 1 or answer > len(answer_hermione): 
            print("This is not  valid choice")
    print("Your choice : ",answer)
    if answer == 1 :
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        change = "Intelligence"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif answer == 2 :
        print("Hermione looks at you in a disappointed way: -I thought u would have been different from the others...\n" \
            "You're finally not special at all.")
        #insert video de moi qui cracvhe sur victor
        change = "Courage"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    print("Then a blonde boy enters, looking arrogant.")

    answer_draco = {"1" : "Shake his hand politely.","2" : "Ignore him completely.","3" : "Respond with arrogance."}
    print("— I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?""\n"
          "How do you respond ? : ")
    for i in answer_draco:
        print(i)
    answer = 0
    while answer < 1 or answer > len(answer_draco):
        answer = input("Your choice : ")
        if answer < 1 or answer > len(answer_draco): 
            print("This is not  valid choice")
    print("Your choice : ",answer)
    if answer == 1 :
        print("Draco is trying not to laugh: -Good boy.")
        change = "Ambition"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif answer == 2 :
        print("Draco frowns, annoyed. — You'll regret that!")
        change = "Loyalty"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)
    elif answer == 3 :
        print("Draco does a backflip and brake the glasse behind him, as he's flying out of the train he's cursing you:\n -YYOoOOuUUuuU MmAAaaADddDEeeE TTtHHHhIIiSssS HHhAAapPPEeeEnNNDD !!!!")
        change = "Courage"
        character[change] += 1
        if not change in changed_attributes:
            changed_attributes.append(change)

    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print("Your choices already say a lot about your personality!""\n"
            "Your updated attributes:",end=" ")
    for i in changed_attributes:
        print(change,character[i],end=" ")
