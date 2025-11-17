from VD_games.cli import welcome_user

from VD_games.engine import run

from VD_games.games.even import generate_question_answer

def is_even(number: int) -> bool:
    return number % 2 == 0


def main() -> None:
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    run(
        generate_question_answer=generate_question_answer,
        check_answer=is_even,
        user_name=user_name,
    )


if __name__ == '__main__':
    main()
