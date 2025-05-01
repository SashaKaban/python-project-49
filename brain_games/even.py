import random

import prompt


def even_func():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_count = 0
    while correct_count != 3:
        number = random.randint(1, 1000)
        print('Question: ' + str(number))
        answer = prompt.string("Your answer: ")
        if number % 2 == 0: 
            even = "yes"
        else:
            even = "no"
        if even == answer:
            correct_count += 1
            print('Correct!')
        else:
            print("Let's try again, Bill!")
            return
    print('Congratulations, ' + name + '!')
