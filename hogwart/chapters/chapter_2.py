import time
from hogwart.chapters.chapter_1 import create_character
from hogwart.utils.input_utils import slow_print
from hogwart.universe.house import assign_house

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

def welcome_message():
    intro = [
    "Mes chers élèves, c’est avec une grande joie que je vous accueille en ce jour mémorable à Poudlard, ce sanctuaire de magie et de savoir. "
    "Vous voici à l’aube d’un voyage extraordinaire, un périple qui vous mènera bien au-delà des limites de ce que vous croyez connaître. "
    "Ici, entre ces murs anciens, se mêlent traditions séculaires et découvertes sans fin. La magie, dans toute sa complexité et sa beauté, vous sera révélée, "
    "non comme une simple force brute, mais comme un art subtil qui requiert patience, sagesse et un cœur pur.",

    "N’oubliez jamais que la véritable magie ne réside pas seulement dans les sorts que vous lancerez, ni dans les potions que vous préparerez, "
    "mais surtout dans les choix que vous ferez. Le courage face à l’adversité, la loyauté envers vos amis, la curiosité insatiable qui pousse à apprendre et à comprendre — "
    "voilà les véritables pouvoirs qui façonneront votre destin. Chaque échec sera une leçon, chaque réussite une pierre ajoutée à l’édifice de votre caractère.",

    "Poudlard est plus qu’une école : c’est une famille, un foyer où l’amitié et la diversité se célèbrent, où la tolérance et le respect sont les fondations invisibles de notre communauté. "
    "Vous apprendrez à travailler ensemble, à vous soutenir dans les moments d’ombre et à partager la lumière.",

    "Alors, avancez avec confiance, portez haut l’étendard de votre maison, mais surtout, écoutez la voix de votre conscience. "
    "Car c’est elle qui guidera vos pas, même lorsque les chemins seront obscurs. Le futur est un livre blanc, prêt à être écrit par vos actions et votre sagesse. "
    "Que cette année à Poudlard soit celle où vous découvrirez non seulement la magie du monde, mais aussi la magie en vous-même."
]

    for paragraph in intro:
        slow_print(paragraph)
        input("\n Appuie sur Entrée pour continuer... \n")

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
    character[house] = house
    slow_print(f"The Sorting Hat exclaims: {house} !\n You join the {house} students to loud cheers !")

sorting_ceremony(player)