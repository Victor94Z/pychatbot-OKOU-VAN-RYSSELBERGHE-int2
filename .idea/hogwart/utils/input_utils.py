def ask_text(question):
    answer = input(question)
    while len(answer) == 0 or answer.isspace():
        answer = input(question).strip()

    return answer

