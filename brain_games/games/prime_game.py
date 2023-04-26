import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    if numb > 1:
        for i in range(2, int(numb / 2) + 1):
            if numb % i == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'


def game():
    number = random.randint(2, 30)
    expression = number
    correct_answer = is_prime(number)
    return {
        'expression': expression,
        'correct_answer': correct_answer,
    }
