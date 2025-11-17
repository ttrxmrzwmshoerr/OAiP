import random


def generate_question_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 8)
    progression = [start + i * step for i in range(length)]
    hidden_pos = random.randint(0, length - 1)
    progression_display = [str(progression[i]) if i != hidden_pos else ".." for i in range(length)]
    question = " ".join(progression_display)
    answer = str(progression[hidden_pos])
    return question, answer
