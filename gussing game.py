import random

def guess(x):
    randomnumber=random.randint(1,x)
    guessnumber=0
    while guessnumber!=randomnumber:
        guessnumber=int(input(f'guess the number between (1,{x})'))
        if guessnumber>randomnumber:
            print(f'the entered number is greater than computer guess number')
        elif guessnumber<randomnumber:
            print(f'the entered number is smaller than computer guess number')
    print("Congrats!!!!your guess was correct")
    print("You won the game")

guess(100)