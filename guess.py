import random
random_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != random_number:
    if guess > random_number:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess again: "))
print("You got the guess")
