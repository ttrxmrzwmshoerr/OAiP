import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question_answer():
    number = random.randint(2, 100)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct
