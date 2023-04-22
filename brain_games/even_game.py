import prompt
from random import randint


def user_name():
    name = prompt.string('May I have your name? ')
    return name


def rand_num():
    return randint(1, 100)


def is_even(numb):
    if numb % 2 == 0:
        return True
    else:
        return False


def game_logic():
    name = user_name()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_count = 0
    while correct_answer_count <= 2:
        number = rand_num()
        print('Question:', number)
        answer = prompt.string('Your answer? ')
        if (is_even(number) and answer == 'yes') \
                or (not is_even(number) and answer == 'no'):
            correct_answer_count += 1
            print('Correct!')
        elif is_even(number) and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif not is_even(number) and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        if correct_answer_count == 3:
            print(f'Congratulations, {name}!')
