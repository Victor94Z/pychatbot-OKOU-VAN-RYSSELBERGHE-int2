
from utils.input_utils import ask_choice

# Create and initialize a character
def init_character(last_name, first_name, attributes) :

    character_init = {
        "Last Name" : last_name,             # Character last name
        "First Name" : first_name,           # Character first name
        "Money" : 100,                       # Starting money
        "Spells" : [],                       # Known spells
        "Inventory" : [],                    # Items owned
        "Attributes": attributes,            # Character attributes
        "House":""                           # Character attributes
    }
    return character_init


# Display all information about the character
def display_player(character):

      print("Character profile:\n")
      print("First Name : ", character["First Name"])
      print("Last Name : ", character["Last Name"])
      print("Money : ", character["Money"])
      print("Spells : ", ", ".join(character["Spells"]))                # Display all spells separate by a comma
      print("Inventory : ", ", ".join(character["Inventory"]))          # Display all items in inventory separate by a comma
      print("Attributes : ")
      for attr, value in character["Attributes"].items():               # Display character attributes with good syntax
          print(f"- {attr}: {value}")
      print("House : ",character["House"])


# Modify the character's money
def modify_money(character,amount):

    # Update money
    character["Money"] += amount
    print()

    #Display result
    if amount > 0 :
        print(f"You have won {amount} galleons !")
        print()
        print("Your money : ",character["Money"])
    else:
        print(f"You have lost {amount} galleons !")
        print()
        print("Your money : ",character["Money"])




# Add an item to the character inventory
def add_item (character, key, item):
    print(f"You found: : {item} ")
    print()

    # Ask player if they want to keep the item
    answer =ask_choice(f"Do you want to add '{item}' to your inventory ?",["Yes","No"])

    # Add item if accepted
    if answer.lower() == "yes" or answer.lower() == "1":
        character[key].append(item)
        print()
        return f"You added {item} to your inventory !"

    # Otherwise, do nothing
    else:
        print()
        return f"No items have been added to your inventory"









