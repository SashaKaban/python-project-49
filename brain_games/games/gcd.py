import random

import prompt


def gcd_func(name):
    print('Find the greatest common divisor of given numbers.')
    correct_count = 0
    while correct_count != 3:
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
            correct_count += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")