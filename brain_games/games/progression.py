import random

import prompt


def progr_func(name):
    print('What number is missing in the progression?')
    correct_count = 0
    while correct_count != 3:
        start = random.randint(1, 50)
        step = random.randint(5, 15)
        length = random.randint(5, 10)
        num_list = []
        next_item = start
        for i in range(length):
            num_list.append(next_item)
            next_item += step
        hidden_element = random.randint(0, length - 1)
        result = num_list[hidden_element]
        num_list[hidden_element] = ".."   
        print(f"Question: {' '.join(str(i) for i in num_list)}")
        answer = prompt.string("Your answer: ")
        if result == int(answer):
            correct_count += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")