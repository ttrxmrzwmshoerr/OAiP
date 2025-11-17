import prompt


MAX_ROUNDS = 3


def run(game_func, name, instruction=""):
    """Движок: 3 раунда с генератором игры."""
    if instruction:
        print(instruction)
    correct_count = 0

    while correct_count < MAX_ROUNDS:
        question, correct = game_func()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer == correct:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
