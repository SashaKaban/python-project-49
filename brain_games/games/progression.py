import random

import prompt


def progr_func():
    start = random.randint(1, 50)
    step = random.randint(5, 15)
    length = random.randint(5, 10)
    num_list = []
    next_item = start
    for _ in range(length):
        num_list.append(next_item)
        next_item += step
    hidden_element = random.randint(0, length - 1)
    result = num_list[hidden_element]
    num_list[hidden_element] = ".."   
    print(f"Question: {' '.join(str(i) for i in num_list)}")
    answer = prompt.string("Your answer: ")
    if result == int(answer):
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
    return False
