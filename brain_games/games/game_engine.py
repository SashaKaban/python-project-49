
import prompt


def engine(func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    if func.__name__ == "prime_func":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if func.__name__ == "gcd_func":
        print('Find the greatest common divisor of given numbers.')
    if func.__name__ == "even_func":
        print('Answer "yes" if the number is even, otherwise answer "no".')
    if func.__name__ == "progr_func":
        print('What number is missing in the progression?')
    if func.__name__ == "calc_func":
        print('What is the result of the expression?') 
    correct_count = 0
    while correct_count != 3:
        if func():
            correct_count += 1
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            return 
    print(f"Congratulations, {name}!")    
