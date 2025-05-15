import random

import prompt


def calc_func(name):
    print('What is the result of the expression?')
    correct_count = 0
    while correct_count != 3:
        a = random.randint(1, 20)
        b = random.randint(1, 10)
        item = random.choice(['+', '-', '*'])
        result = eval(f"{str(a)} {item} {str(b)}")
        print(f"Question: {str(a)} {item} {str(b)}")
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            correct_count += 1
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")