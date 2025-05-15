import random

import prompt


def gcd_func():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"Question: {str(a)} {str(b)}")
    answer = prompt.string("Your answer: ")
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = a + b
    if result == int(answer):
        return True
    print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
    return False