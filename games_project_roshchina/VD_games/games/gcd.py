import random
from math import gcd


def generate_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct = gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct)
