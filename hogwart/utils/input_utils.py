import json
import os
import time

# Print like a typewriter
def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Ask the user for a non-empty text input
def ask_text(question):

    # Get user input and remove extra spaces
    answer = input(question).strip()

    # Ask again if input is empty or only spaces
    while len(answer) == 0 or answer.isspace():
        answer = input(question).strip()

    return answer


# Ask the user to choose an option from a list
def ask_choice(question, choices_list):
    print(question)
    print()

    size_list = len(choices_list)
    values_and_index = []

    # Display all choices
    for i in range(size_list):
        print(f"{i + 1}. {choices_list[i]}")

        # Store valid answers (text and number)
        values_and_index.append((choices_list[i].lower()))
        values_and_index.append(str(i + 1).lower())

    print()
    print("Your choice:", end=" ")
    answer = input()
    answer = answer.strip()

    # Repeat until a valid choice is entered
    while answer.lower() not in values_and_index:
        print()
        print("Your choice have to be in the list :", end=" ")
        answer = input()


    return answer.strip()


# Build the full path to a data file ( given by the teacher to replace the opening with 'with' that wasn’t working )
def build_file_path(file_name):

    # Folder where this file is located
    current_dir = os.path.dirname(__file__)

    # Go up one level (hogwart/)
    base_dir = os.path.dirname(current_dir)

    # build full path: hogwart/data/file_name
    file_path = os.path.join(base_dir, "data", file_name)

    return file_path


# Load and return JSON file content
def load_file(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


# Validate if a string represents a valid number ( verify different cases for ask_number / separate function for readability )
def validate_number(answer, min_val=None, max_val=None):
    is_valid_number = True

    # Check answer not empty
    if len(answer) == 0 or answer.isspace():
        is_valid_number = False
        return is_valid_number,answer

    # Check if the answer is negative
    is_negative = False
    abs_index = 0

    if answer[0] == '-':
        is_negative = True
        abs_index = 1
        if len(answer) == 1:
            is_valid_number = False
            return is_valid_number,answer

    # Check if each character is a valid digit
    for char in answer[abs_index:]:
        if char < '0' or char > '9':
            is_valid_number = False
            return is_valid_number,answer


    # Convert answer to int with the method given
    converted_answer = 0
    for c in answer[abs_index:]:
        digit = ord(c) - ord('0')
        converted_answer = converted_answer * 10 + digit

    if is_negative:
        converted_answer = -converted_answer

    # Check range if provided
    if min_val is not None:
        if converted_answer < min_val:
            is_valid_number = False
            return is_valid_number,converted_answer

    if max_val is not None:
        if converted_answer > max_val:
            is_valid_number = False
            return is_valid_number,converted_answer

    return is_valid_number,converted_answer


# Ask the user for a valid number
def ask_number(message, min_val=None, max_val=None):

    # Swap bounds if min is greater than max
    if min_val is not None and max_val is not None:
        if min_val > max_val:
            min_val,max_val = max_val,min_val

    # First input
    answer=input(message).strip()

    # Build error message
    error_message = "Please enter a number"
    if min_val is not None and max_val is not None:
        error_message += " between " + str(min_val) + " and " + str(max_val)
    elif min_val is not None and max_val is None:
        error_message += " higher than " + str(min_val)
    elif min_val is None and max_val is not None:
        error_message += " lower than " + str(max_val)

    error_message += " : "

    # Number validation
    is_valid_number, converted_answer = validate_number(answer, min_val, max_val)

    # Repeat until valid
    while not is_valid_number:
        answer = input(error_message).strip()
        is_valid_number, converted_answer = validate_number(answer, min_val, max_val)


    return converted_answer


