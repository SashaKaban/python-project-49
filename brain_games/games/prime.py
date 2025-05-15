import math

import prompt

import random


def prime_func():
    number = random.randint(1, 100)
    print(f"Question: {str(number)}")
    answer = prompt.string("Your answer: ") 
    if number <= 1:
        result = "no"
        if result == answer:
            return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            result = "no"
            if result == answer:
                return True
    result = "yes"
    if result == answer:
        return True