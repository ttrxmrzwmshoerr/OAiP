from VD_games.cli import welcome_user
from VD_games.engine import run
from VD_games.games.calc import generate_question_answer


def main():
    name = welcome_user()
    run(generate_question_answer, name, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
