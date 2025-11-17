import random
import operator

OPERATIONS = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def generate_question_answer():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    op = random.choice(list(OPERATIONS.keys()))
    correct = OPERATIONS[op](num1, num2)
    question = f"{num1} {op} {num2}"
    return question, str(correct)
