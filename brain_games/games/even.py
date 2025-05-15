import random

import prompt


def even_func():
    number = random.randint(1, 100)
    print(f"Question: {str(number)}")
    answer = prompt.string("Your answer: ")
    if number % 2 == 0: 
        result = "yes"   
    else:
        result = "no"
    if answer == result:
        return True
    return False