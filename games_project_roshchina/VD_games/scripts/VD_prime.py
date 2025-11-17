from VD_games.cli import welcome_user
from VD_games.engine import run
from VD_games.games.prime import generate_question_answer


def main():
    name = welcome_user()
    run(generate_question_answer, name, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
