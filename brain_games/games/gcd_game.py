import random
import math


question = 'Find the greatest common divisor of given numbers.'


def game():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    expression = f'{number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return {
        'expression': expression,
        'correct_answer': correct_answer,
    }
