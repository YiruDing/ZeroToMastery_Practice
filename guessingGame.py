import sys, random

# count = 3
# num = sys.argv[1]
# answer = random.randint(1,20)
# while count:
#     if num == answer:
#         print('You got the right answer!')
#     else:
#         print('Try again')
#         count -= 1

answer = random.randint(1, 10)
# answer = random.randint(sys.argv[1],sys.argv[2])
while True:
    try:
        guess = int(input('Guess the number 1-10 : '))
        if 0 < guess < 11:
            if guess == answer:
                print('Right answer!')
                break
        else:
            print('Please insert a number between 1 and 10')
    except ValueError:
        print('Please enter a number')
        continue