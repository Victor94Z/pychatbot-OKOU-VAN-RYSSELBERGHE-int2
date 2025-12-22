import random

from hogwart.universe.house import update_house_points, display_winning_house
from hogwart.utils.input_utils import load_file, build_file_path, slow_print
from hogwart.universe.character import display_player

TEAMS_QUIDDITCH_PATH = build_file_path("teams_quidditch.json")

# Load data
teams_quidditch = load_file(TEAMS_QUIDDITCH_PATH)


# CHAPTER 4 : Quidditch match

# Create the teams
def  create_team(house, team_data, is_player=False, player=None):

    #Initialise team
    team = {
        'name': house,
        'score': 0,
        'has_scored': 0,
        'has_stopped': 0,
        'caught_snitch': False,
        'players': []
    }

    if is_player and player is not None:
        players = [player["First Name"] + "(Seeker)"]
        players += teams_quidditch[house]['players'][1:]
        team['players'] = players
    else:
        team['players'] = teams_quidditch[house]['players']

    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal=random.randint(1,10)

    if chance_goal <= 6:
        if player_is_seeker:
            scorer=attacking_team['players'][0]
        else:
            scorer=random.choice(attacking_team['players'][1:])
        attacking_team['score']+=10
        attacking_team['has_scored']+=1
        slow_print(f"{scorer} scores a goal for {attacking_team['name']}! (+10 points)")

    else:
        defending_team['has_stopped']+=1
        slow_print(f"{defending_team['name']} blocks the attack!")




def golden_snitch_appears():
    if random.randint(1,6)==6:
        return True
    return False

def catch_golden_snitch(e1,e2) :
    winning_team = random.choice([e1,e2])
    winning_team['score']+=150
    winning_team['caught_snitch'] = True

    return winning_team

def display_score(e1, e2):
    print("\nCurrent score:\n")
    print(f"→ {e1["name"]} : {e1['score']} points" )
    print(f"→ {e2["name"]} : {e2['score']} points" )

def display_team(house, team):
    print(f"\n{house} team :\n")
    for player in team:
        print(f"- {player}")

def quidditch_match(character, houses):

    global team_who_win, update_houses

    slow_print("\nQuidditch Match: Slytherin vs Hufflepuff! \n")
    player_team_name = character['House']
    opponent_team_name = random.choice([house for house in houses.keys() if house != player_team_name])
    player_team=create_team(player_team_name,teams_quidditch,True,character)
    opponent_team=create_team(opponent_team_name,teams_quidditch)
    display_team(player_team_name,player_team['players'])
    display_team(opponent_team_name,opponent_team['players'])

    slow_print(f"\nYou are playing for {player_team_name} as the Seeker \n")
    print(input("\nPress Enter to continue...\n"))
    slow_print('{:^130}'.format("The referee raises their wand.\n"))
    slow_print('{:^130}'.format("With a flash of light, the Bludgers and the Quaffle are released into the air.\n"))
    slow_print('{:^130}'.format("\nThe match begins!\n"))


    rounds=1
    golden_snitch_catch= False
    while (rounds <=20) and not golden_snitch_catch:
        print(f"\n ━━━━━━━━━━━━ Turn {rounds} ━━━━━━━━━━━━\n")
        attempt_goal(player_team, opponent_team,True)
        attempt_goal(opponent_team,player_team)
        display_score(player_team,opponent_team)
        appears = golden_snitch_appears()
        if appears:
            slow_print("\nA sudden glimmer catches everyone's attention…\n")
            slow_print("The Golden Snitch has appeared!\n")
            team_who_win=catch_golden_snitch(player_team,opponent_team)
            team_who_win['score'] += 150
            print(f"The Golden Snitch has been caught by {team_who_win['name']}! (+150 points)")
            golden_snitch_catch = True

        print(input("\nPress Enter to continue..."))
        rounds+=1


    slow_print("\nEnd of the match!")
    slow_print("\nThe final whistle echoes through the stadium.")
    slow_print("Brooms slowly descend as the crowd erupts into applause.\n")
    print(input("Press Enter to continue..."))

    display_score(player_team,opponent_team)
    slow_print("\nFinal result :")
    if golden_snitch_catch :
        slow_print(f"The Golden Snitch was caught by {team_who_win['name']}! ")
        update_houses = update_house_points(houses, team_who_win['name'], team_who_win['score'])
        print()

    if player_team["score"] > team_who_win["score"]:
        team_who_win=player_team
    else:
        team_who_win=opponent_team

    slow_print(f"The winning house is {team_who_win["name"]} with {team_who_win['score']} points! ")
    slow_print(f"Victory for {team_who_win['name']}! ")
    update_houses = update_house_points(update_houses, team_who_win['name'], 500)
    print()
    display_winning_house(update_houses)
    return update_houses

def start_chapter_4_quidditch(character, houses):
    slow_print('{:^130}'.format("\nChapter 4 : Quidditch match !\n"))
    slow_print('{:^130}'.format("The stadium roars as the two houses take their positions.\n"))
    slow_print('{:^130}'.format("Brooms are ready, eyes are sharp, and the Golden Snitch is about to be released.\n"))
    slow_print('{:^130}'.format("This match will decide the fate of the House Cup…\n"))
    update_house=quidditch_match(character, houses)
    slow_print('{:^130}'.format("\nEND OF CHAPTER 4\n"))
    slow_print('{:^130}'.format("What an incredible performance on the field!\n"))
    slow_print('{:^130}'.format("Courage, strategy, and determination made this match unforgettable.\n"))
    slow_print('{:^130}'.format("The fate of the House Cup has now been decided…\n"))

    print(input("Press Enter to continue...\n"))
    slow_print("After an intense season of challenges and competition")
    display_winning_house(update_house)
    slow_print("Congratulations to all its members\n")
    print(input("Press Enter to continue...\n"))
    display_player(character)

    return update_house












