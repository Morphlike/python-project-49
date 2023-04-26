import random
import math


question = 'What number is missing in the progression?'


def game():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 5)
    finish = start + length * step
    result = [i for i in range(start, finish, step)]
    position = random.randint(0, len(result) - 1)
    correct_answer = str(result[position])
    result[position] = '..'
    expression = " ".join(map(str, result))
    return {
        'expression': expression,
        'correct_answer': correct_answer,
    }
