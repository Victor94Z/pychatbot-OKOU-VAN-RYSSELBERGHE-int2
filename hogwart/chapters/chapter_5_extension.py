import random
import time

from universe.character import display_player
from utils.input_utils import slow_print, ask_choice, load_file, build_file_path
from chapters.chapter_1 import create_character


# Path to spells data file
SPELLS_DATA_PATH = build_file_path("spells.json")

# Load spells data
spells = load_file(SPELLS_DATA_PATH)


def get_spells_by_type(character, spell_type):

    indices = []

    for spell_name in character["Spells"]:
        for i in range(len(spells)):
            if spells[i]["name"] == spell_name and spells[i]["type"] == spell_type:
                indices.append(i)

    return indices

def get_spell_by_name(spell_name):

    for spell in spells:
        if spell["name"] == spell_name:
            return spell
    return None

def choose_spell(spell_indices, prompt):
    slow_print(prompt)

    names = []
    numbers = []

    i = 1
    for spell_index in spell_indices:
        spell_name = spells[spell_index]['name']
        print(f"{i}. {spell_name}")
        names.append(spell_name)
        numbers.append(str(i))
        i += 1

    choice = ask_choice("Choose a spell:", names )


    if choice in numbers:
        return names[int(choice) - 1]

    return choice



def spider_combat(character):

    player_health = 100
    spider_health = 50
    spider_damage = 30

    attack_spells = get_spells_by_type(character, "Offensive")
    defense_spells = get_spells_by_type(character, "Defensive")
    slow_print("A giant spider jump on you from the darkness!")

    if not attack_spells:
        slow_print("You have no offensive spells... You flee in panic.")
        return False

    while player_health > 0 and spider_health > 0:
        spider_turn = random.choice([True, False])
        action = ask_choice('Do you want to "attack" or "defend" ?', ["attack", "defend"])

        if action.lower() == "attack" or action.lower() == "1":
            spell_name= choose_spell(attack_spells, "Your offensive spells:")
            spell = get_spell_by_name(spell_name)

            damage = random.randint(20, 30)
            spider_health -= damage
            slow_print(
                f"You {spell['description']} "
                f"The spider loses {damage} health."
            )

        elif (action.lower() == "defend" or action.lower() == "2" ) and defense_spells:
            spell_name = choose_spell(defense_spells, "Your defensive spells:")
            spell = get_spell_by_name(spell_name)

            slow_print(f"You {spell['description']}")
            if spider_turn:
                reduced = spider_damage // 2
                player_health -= reduced
                slow_print(f"The spider hits you, but you reduce the damage to {reduced}.")
                spider_turn = False
            else:
                slow_print("The spider doesn't seem willing to attack")


        if spider_turn and spider_health > 0:
            player_health -= spider_damage
            slow_print(f"The spider bites you! You lose {spider_damage} health.")

        slow_print(f"Your health: {player_health} | Spider health: {spider_health}")
        time.sleep(1)

    if player_health > 0:
        slow_print("You defeated the spiders and collect a spider eye.")
        character["Inventory"].append("spider eye")
        print()
        slow_print(f"You rest for a while and regain your health points")
        print()
        return True
    else:
        slow_print("You collapse... everything fades to black.")
        return False



def explore_forest(character):
    slow_print(
        "The Forbidden Forest is dark and silent.\n"
        "You feel watched."
    )

    good_path = []

    i = 0
    while i < 3:
        good_path.append(str(random.randint(1, 3)))
        i += 1

    luck = 0

    for step in range(3):
        choice = ask_choice("Three paths lie ahead. Which one do you choose?",["1", "2", "3"])

        if choice == good_path[step]:
            slow_print("You chose the right path... for now.")
            luck += 1
        else:
            survived = spider_combat(character)
            if not survived:
                return False

    if luck == 3:
        slow_print(
            "You discover a peaceful lake.\n"
            "A strange wand floats on the surface."
        )
        pickup = ask_choice("Do you pick it up?", ["yes", "no"])
        if pickup == "yes" or pickup == "1":
            slow_print("You obtained the Supreme Sorcerer Wand.")
            character["Inventory"].append("supreme sorcerer wand")

    return True


def start_chapter_5(character):
    slow_print(
        "\nAs you walk through the corridors of Hogwarts,\n"
        "dark smoke rises from the Forbidden Forest."
    )

    approach = ask_choice("Are you interested in going into the forest?",["yes", "no"])

    if approach.lower() == "no" or approach.lower() == "2":
        slow_print("You decide not to take the risk.")
        print()
        print(('{:^130}'.format("GAME OVER")))
        exit()

    enter = ask_choice("This is the Forbidden Forest. Are you sure?",["yes", "no"])

    if enter.lower() == "yes" or enter.lower() == "1":
        survived = explore_forest(character)
        if not survived:
            slow_print(
                "You wake up in Hagrid's hut.\n"
                "The forest looms outside the window."
            )
            print()
            print(('{:^130}'.format("GAME OVER")))
            exit()

        else:
            slow_print("\nYou have finished the game, congratulations")
            print(('{:^130}'.format("END")))
            exit()
    else:
        slow_print("You turn back, your instincts screaming at you.")
        print()
        print(('{:^130}'.format("GAME OVER")))
        exit()


