import random
import sys
from typing import NoReturn


def is_even(number: int) -> bool:
    return number % 2 == 0


def play_game() -> None:
    print("Welcome to the VD-games!")
    name = input("May I have your name? ").strip() or "Player"
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct = 0
    while correct < 3:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = input("Your answer: ").strip().lower()

        expected = "yes" if is_even(num) else "no"

        if answer not in {"yes", "no"}:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
            print(f"Let's try again, {name}!")
            return

        if answer == expected:
            print("Correct!")
            correct += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main() -> NoReturn:
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted. Goodbye!")
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
