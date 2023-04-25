import prompt


def get_answer():
    return prompt.string('Your answer? ')


def correct(expected, given):
    if expected == given:
        return True
    else:
        return False


def game_engine(source):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(source.question)
    correct_answer_count = 0
    while correct_answer_count < 3:
        play = source.game()
        expression = play['expression']
        print('Question:', expression)
        answer = get_answer()
        correct_answer = play['correct_answer']
        if correct(correct_answer, answer):
            correct_answer_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        if correct_answer_count == 3:
            print(f'Congratulations, {name}!')
