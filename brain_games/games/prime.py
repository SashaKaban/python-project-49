import math
import random

import prompt


def prime_func():
    number = random.randint(1, 100)
    print(f"Question: {str(number)}")
    answer = prompt.string("Your answer: ") 

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    if is_prime(number):
        result = "yes"
    else:
        result = "no"
    if result == answer:
        return True