import random


question = 'What is the result of the expression?'


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def game():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    choices = [add, multiply, subtract]
    math_op = random.choice(choices)
    symbol = '+' if math_op is add else '-' if math_op is subtract else '*'
    expression = f'{number1} {symbol} {number2}'
    correct_answer = str(math_op(number1, number2))
    return {
        'expression': expression,
        'correct_answer': correct_answer,
    }
