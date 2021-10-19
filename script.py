import random

def run_guess(guess, answer):
    if 0 < guess<11:
            if guess == answer:
                print('Right answer!')
                return True
    else:
                print('Please insert a number between 1 and 10')

if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('Guess the number 1-10 : '))
            if(run_guess(guess, answer)):
                print('Right answer!')
                break
            else:
                print('Please insert a number between 1 and 10')
        except ValueError:
            print('Please enter a number')
            continue
