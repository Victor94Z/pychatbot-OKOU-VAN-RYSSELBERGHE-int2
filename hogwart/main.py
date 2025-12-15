from hogwart.chapters.chapter_1 import introduction,create_character,buy_supplies,meet_hagrid,receive_letter

# CHAPTER 1
introduction()
character=create_character()
receive_letter()
print(input("Press Enter to continue..."))
meet_hagrid(character)
buy_supplies(character)