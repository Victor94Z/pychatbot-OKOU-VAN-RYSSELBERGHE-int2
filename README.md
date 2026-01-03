# pychatbot-OKOU-VAN-RYSSELBERGHE-int2
#
# 1. General Presentation: 
#
# - Project Title : "Hogwarts Project : The Art of Coding like a Wizard"

# - Brief Description : The game consists of creating a wizard, being sorted into a house, learning spells, and experiencing magical adventures, including a Quidditch match and a heroic battle.

# - Contributors : OKOU Victor , VAN RYSSELBERGHE

# - Installation : 
# -> Install PyCharm and connect to GitHub, making sure to use the Efrei license.
# -> Configure a Python interpreter beforehand.
# -> Copy the GitHub repository link.
# -> Open PyCharm, create a new project, paste the repository link, and click Create

# Usage: 
# Open the main.py file.
# Run the program by clicking RUN (green arrow).

# Key Features: 
# Interactive interface
# Player choices that provide full immersion in the Hogwart universe

# Logbook :
# Week 1: Project architecture setup, Git repository creation, and implementation of Chapter 1 (Shopping in Diagon Alley).
# Week 2: Development of the house.py module, the input_utils module and the character.py module, and Chapter 2 (Hogwarts Express & Sorting).
# Week 3: Finalization of Chapter 3 (Spells & Quiz) and Interim Submission on December 21, 2025  .
# Week 4: Implementation of the Quidditch feature and extension (Chapter 5), final tests, and writing of this README.

# Task Distribution :
# Chapter 1 : Victor
# Chapter 2 : Adhenis 
# Chapter 3 : Victor
# Chapter 4 : Victor
# Chapter 5 : Adhenis
# Other elements : Together
# Additional communication took place on Teams to ensure a balanced workload.

# Control, Testing, and Validation :

# Input and Error Management : The program includes dedicated input validation functions to ensure robust user interaction and prevent runtime errors.
# Input Control: User inputs are handled through specific utility functions, notably:
# -> demander_nombre: ensures that numeric inputs fall within the expected range and repeatedly prompts the user until a valid value is provided.
# -> demander_texte: validates textual input and prevents empty or invalid entries.
# Error Handling: The code systematically checks user input types and value ranges before processing them. Invalid inputs (such as non-numeric values or out-of-range numbers) are rejected, and the user is prompted to enter a valid value. This approach prevents crashes and ensures a smooth execution flow.
# Known Bugs: At the time of submission, no known bugs or critical errors have been identified.

# Testing Strategies: 
# Test Cases: Multiple test cases were conducted to validate each major feature of the game, including:
# -> Character creation and house sorting
# -> Spell selection and quiz evaluation
# -> Quidditch match simulation
# -> Final combat mechanics
# Each test verified correct program behavior under both normal and edge-case inputs.
# Testing Results: All tested scenarios produced the expected outcomes, confirming the correctness and stability of the implemented features.
# Validation Evidence: Screenshots are provided below to illustrate specific test executions and validate the behavior of key parts of the code.

# Screenshots : Screenshots demonstrating the execution of selected test cases and validations:
# Screenshot #1: Input Validation (ERROR CASE)
# Objective: demonstrate error handling

# Screenshot #2: Input Validation (SUCCESS CASE)
# Objective: show that valid input is accepted

# Screenshot #3: Testing a Key Feature
# Objective : Test the choice of the house

# Screenshot #4: End of Game / Final Scenario
# Objective: demonstrate that the game runs to completion without errors