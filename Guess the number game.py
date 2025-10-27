import random
number = random.randint(1, 50)
guess = None

print("Hey you lets play the 'guess the number' game!!!")
while guess != number:
    try:
        guess = int(input("Guess a number between 1 and 50: "))

        if guess < number:
            print("Too low, try again!!")
        elif guess > number:
            print("Too high, try again!!")
        else:
            print(f"Congrats you finally guessed the number!!")
    except ValueError:
        print("Enter a valid number!")