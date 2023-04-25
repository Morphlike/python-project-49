import random

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(numb):
    if numb % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game():
    number = random.randint(1, 100)
    expression = number
    correct_answer = is_even(number)
    return {
        'expression': expression,
        'correct_answer': correct_answer,
    }
