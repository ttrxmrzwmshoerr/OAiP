import random


def generate_question_answer():
    number = random.randint(1, 100)
    correct = "yes" if number % 2 == 0 else "no"
    return str(number), correct
	
