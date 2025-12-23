from hogwart.utils.input_utils import slow_print,ask_choice


def spider_fight():
    slow_print('{:^130}'.format("As you're walking through the corridor in Poudlard you see a dark smoke coming out of a forest.\n" 
    "Looking closely the whole forest is suspicious emaning an odd energy."))
    approach = ask_choice("Are you interested in going in the forest ?",["yes","no"])
    if approach == "yes":
        print('{:^130}'.format("Your are approaching the forest when a sign on the side trigger your attention.\n" 
        " ________________________________________________________ \n" 
        "|                                                        |\n" 
        "|         ___                  ___    ___  __            |\n" 
        "|        |   \    /\    |\  | /   \  |    |__\           |\n" 
        "|        |    |  /__\   | \ ||  ____ |--- | \            |\n"  
        "|        |___/  /    \  |  \| \___/  |___ |  \           |\n" 
        "|                                                        |\n" 
        "|                                                        |\n" 
        "|________________________________________________________|\n" ))
        enter = ask_choice("This is the forbidden forest entrance, are your sure you want to continue your way through ? :",['yes','no'])
        if enter == "yes":
            slow_print('{:^130}'.format("The player enter the Forbidden forest"))
spider_fight()