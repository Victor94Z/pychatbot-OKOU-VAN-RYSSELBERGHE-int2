from hogwart.chapters.chapter_1 import start_chapter_1
from hogwart.chapters.chapter_2 import start_chapter_2
from hogwart.chapters.chapter_3 import start_chapter_3

# CHAPTER 1
def main():
    character = start_chapter_1()
    houses=start_chapter_2(character, houses = { "Gryffindor": 0,"Slytherin": 0,"Hufflepuff": 0,"Ravenclaw": 0})
    start_chapter_3(character, houses)

main()
