import random

import prompt


def calc_func():
    a = random.randint(1, 20)
    b = random.randint(1, 10)
    item = random.choice(['+', '-', '*'])
    result = eval(f"{str(a)} {item} {str(b)}")
    print(f"Question: {str(a)} {item} {str(b)}")
    answer = prompt.string("Your answer: ")
    if result == int(answer):
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
    return False