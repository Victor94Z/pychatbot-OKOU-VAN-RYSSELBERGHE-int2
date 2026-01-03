from hogwart.utils.input_utils import slow_print,ask_choice, load_file
from hogwart.chapters.chapter_1 import create_character
import random,time, os
from hogwart.universe.character import BASE_DIR


SPELLS_DATA_PATH = os.path.join(BASE_DIR, "data", "houses.json")
spells = load_file(SPELLS_DATA_PATH)

player = create_character()

def spider_fight(character):
    slow_print('{:^130}'.format("As you're walking through the corridor in Poudlard you see a dark smoke coming out of a forest.\n" 
    "Looking closely the whole forest is suspicious emaning an odd energy."))
    approach = ask_choice("Are you interested in going in the forest ?",["yes","no"])
    if approach == "yes":
        print('{:^130}'.format("Your are approaching the forest when a sign on the side trigger your attention.\n" 
        " ________________________________________________________  \n", 
        "|                                                        | \n", 
        "|         ___                  ___    ___  __            | \n", 
        "|        |   \    /\    |\  | /   \  |    |__\           | \n",
        "|        |    |  /__\   | \ ||  ____ |--- | \            | \n",  
        "|        |___/  /    \  |  \| \___/  |___ |  \           | \n", 
        "|                                                        | \n",
        "|                                                        | \n", 
        "|________________________________________________________| \n",
        "                       |    |                              \n", 
        "                       |    |                              \n",
        "                       |    |                                " ))
        enter = ask_choice("This is the forbidden forest entrance, are your sure you want to continue your way through ? :",['yes','no'])
        if enter == "yes":
            slow_print('{:^130}'.format("The player enter the Forbidden forest \n" 
            "You have the strange impression that something is observing you...\n" 
            "As you look left and right little red dots in the forest disappear cracking the dry leaves"))
            good_path = [random.randint(1,3),random.randint(1,3),random.randint(1,3)]
            luck = 0
            spider_health = 17
            for i in range(3):
                char_path = ask_choice('{:^130}'.format("Three paths are in front of you, which one are choosing ? : ",[1,2,3]))
                if char_path == good_path[i]:
                    spider_health *= 2,5
                    spider_damage = 6
                    slow_print('{:^130}'.format("The grass become taller and the light is struggling to pass through the trees.\n" \
                    "More eyes are looking at you from the dark but you are safe. \n" 
                    "for now... \n",time.sleep(2)))
                    luck += 1
                else :
                    slow_print('{:^130}'.format("You take a branch to go on your way. \n" 
                    "The atmosphere is becoming more and more stressful. You continue straight and... \n" 
                    "CRACK ! \n" 
                    "three spider jumps on you from the dark !")) 
                    player_health = 100

                    attack_spells = []
                    for i in character["Spells"]:
                                if spells[i]["type"] == "Offensive":
                                    attack_spells.append(i)

                    defense_spells = []
                    for i in character["Spells"]:
                                if spells[i]["type"] == "Offensive":
                                    defense_spells.append(i)
                    fight = True
                    while fight:
                        spider_turn = random.choice(True,False)
                        print(spider_turn)
                        action = ask_choice('Do you "attack" or "defend" : ',['attack','defend'])
                        if action == 'attack':
                            possible_spells = []
                            slow_print("Your attack spells are : ")
                            for j in range(len(attack_spells)):
                                possible_spells.append(j)
                                print(j + 1 ,attack_spells[j])
                            spells_used = ask_choice("What spell are you attacking the spider with ? : ",possible_spells)
                            spider_health -= spells[attack_spells[spells_used]]["damage"]//3
                            if spider_health > 0 :
                                slow_print(f"You {spells[attack_spells[spells_used]]["description"]}, the spider still have {spider_health} health")
                            else :
                                slow_print(f"You {spells[attack_spells[spells_used]]["description"]}, You killed the spiders \n"
                                                "you retrieved an eye from the spiders")
                                character["Inventory"].append("spider eye")
                                fight = False
                            if spider_turn:
                                slow_print("Ths spiders jumps on you biting everything they can")
                                player_health -= spider_damage
                                if player_health > 0:
                                    slow_print(f"You lost {spider_damage} health, you still have {player_health} health remaining.")
                                if player_health < 0:
                                      slow_print(f"You lost {spider_damage},you died...")
                                      fight = False
                        if action == "defense":
                            possible_spells = []
                            slow_print("Your defense spells are : ")
                            for j in range(len(defense_spells)):
                                possible_spells.append(j)
                                print(j + 1, defense_spells[j])
                            spells_used = ask_choice("What spell are you attacking the spider with ? : ",possible_spells)
                            if spider_turn:
                                slow_print(f"You {spells[attack_spells[spells_used]]["description"]}")
                            else:
                                slow_print("You blocked nothing, the spiders wait for you to end the spells and attacks you")
                                player_health -= spider_damage * 1.5
                                if player_health > 0:
                                    slow_print(f"You lost {spider_damage} health, you still have {player_health} health remaining.")
                                if player_health < 0:
                                    slow_print(f"You lost {spider_damage},you died...")
                                    fight = False
            if player_health > 0:
                if luck == 3:
                    slow_print(f"You find a peacefull lake that seems alone in its own world. You feel a warm and reassuring sun ray \n"
                                "a strange wood stick is floating upon the lake.")
                    pickup = ask_choice("Do you want to pick it up",["yes","no"])
                    if pickup == "yes":
                        slow_print("You pick up the supreme sorcerer wand")
                        character["Invetory"].append("supreme sorcerer wand")
            else:
                slow_print("You wake up in Hagrid's house. You can see the forbidden forest through the glass")
        else :
            slow_print('{:^130}'.format("petite sasa"))
    else :
        slow_print('{:^130}'.format("bahah t'es une petite sasa"))

        
spider_fight(player)