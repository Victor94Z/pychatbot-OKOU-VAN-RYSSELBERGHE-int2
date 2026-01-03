import random
import time
import os
from hogwart.utils.input_utils import slow_print, ask_choice, load_file
from hogwart.chapters.chapter_1 import create_character
from hogwart.universe.character import BASE_DIR


# =======================
# Chargement des données
# =======================

SPELLS_DATA_PATH = os.path.join(BASE_DIR, "data", "spells.json")
spells = load_file(SPELLS_DATA_PATH)


# =======================
# Fonctions utilitaires
# =======================

def get_spells_by_type(character, spell_type):
    """Retourne les indices de sorts du personnage correspondant au type."""
    return [
        i for i in character["Spells"]
        if spells[i]["type"] == spell_type
    ]


def choose_spell(spell_indices, prompt):
    """Affiche les sorts et permet d'en choisir un."""
    slow_print(prompt)
    for idx, spell_index in enumerate(spell_indices, start=1):
        print(f"{idx}. {spells[spell_index]['name']}")
    choice = ask_choice("Choose a spell :", list(range(1, len(spell_indices) + 1)))
    return spell_indices[choice - 1]


# =======================
# Combat
# =======================

def spider_combat(character):
    player_health = 100
    spider_health = 50
    spider_damage = 8

    attack_spells = get_spells_by_type(character, "Offensive")
    defense_spells = get_spells_by_type(character, "Defensive")

    if not attack_spells:
        slow_print("You have no offensive spells... You flee in panic.")
        return False

    slow_print("Three giant spiders jump on you from the darkness!")

    while player_health > 0 and spider_health > 0:
        spider_turn = random.choice([True, False])
        action = ask_choice('Do you want to "attack" or "defend" ?', ["attack", "defend"])

        if action == "attack":
            spell_index = choose_spell(attack_spells, "Your offensive spells:")
            damage = random.randint(8, 15)
            spider_health -= damage
            slow_print(
                f"You {spells[spell_index]['description']} "
                f"The spider loses {damage} health."
            )

        elif action == "defend" and defense_spells:
            spell_index = choose_spell(defense_spells, "Your defensive spells:")
            slow_print(f"You {spells[spell_index]['description']}")
            if spider_turn:
                reduced = spider_damage // 2
                player_health -= reduced
                slow_print(f"The spider hits you, but you reduce the damage to {reduced}.")
                spider_turn = False

        if spider_turn and spider_health > 0:
            player_health -= spider_damage
            slow_print(f"The spider bites you! You lose {spider_damage} health.")

        slow_print(f"Your health: {player_health} | Spider health: {spider_health}")
        time.sleep(1)

    if player_health > 0:
        slow_print("You defeated the spiders and collect a spider eye.")
        character["Inventory"].append("spider eye")
        return True
    else:
        slow_print("You collapse... everything fades to black.")
        return False


# =======================
# Exploration
# =======================

def explore_forest(character):
    slow_print(
        "The Forbidden Forest is dark and silent.\n"
        "You feel watched."
    )

    good_path = [random.randint(1, 3) for _ in range(3)]
    luck = 0

    for step in range(3):
        choice = ask_choice(
            "Three paths lie ahead. Which one do you choose?",
            [1, 2, 3]
        )

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
        if pickup == "yes":
            slow_print("You obtained the Supreme Sorcerer Wand.")
            character["Inventory"].append("supreme sorcerer wand")

    return True


# =======================
# Scène principale
# =======================

def spider_fight(character):
    slow_print(
        "As you walk through the corridors of Hogwarts,\n"
        "dark smoke rises from the Forbidden Forest."
    )

    approach = ask_choice(
        "Are you interested in going into the forest?",
        ["yes", "no"]
    )

    if approach == "no":
        slow_print("You decide not to take the risk.")
        return

    enter = ask_choice(
        "This is the Forbidden Forest. Are you sure?",
        ["yes", "no"]
    )

    if enter == "yes":
        survived = explore_forest(character)
        if not survived:
            slow_print(
                "You wake up in Hagrid's hut.\n"
                "The forest looms outside the window."
            )
    else:
        slow_print("You turn back, your instincts screaming at you.")


# =======================
# Lancement
# =======================

player = create_character()
spider_fight(player)
