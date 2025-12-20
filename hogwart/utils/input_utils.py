import json
import time 

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def ask_text(question):

    answer = input(question).strip()
    while len(answer) == 0 or answer.isspace():
        answer = input(question).strip()

    return answer



def ask_choice(question, choices_list):
    print(question)
    print()
    size_list = len(choices_list)
    values_and_index = []
    for i in range(size_list):
        print(f"{i + 1}. {choices_list[i]}")

        values_and_index.append((choices_list[i].lower()))
        values_and_index.append(str(i + 1).lower())

    print()
    print("Your choice:", end=" ")
    answer = input()
    answer = answer.strip()

    while answer.lower() not in values_and_index:
        print()
        print("Your choice have to be in the list :", end=" ")
        answer = input()


    return answer.strip()


def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

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

    # Check if each char is a valid digit
    for char in answer[abs_index:]:
        if char < '0' or char > '9':
            is_valid_number = False
            return is_valid_number,answer


    # Convert answer to int
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

def ask_number(message, min_val=None, max_val=None):

    #Swap bounds if not valid
    if min_val is not None and max_val is not None:
        if min_val > max_val:
            min_val,max_val = max_val,min_val

    answer=input(message).strip()

    # Determine error message
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
    while not is_valid_number:
        answer = input(error_message).strip()
        is_valid_number, converted_answer = validate_number(answer, min_val, max_val)


    return converted_answer


