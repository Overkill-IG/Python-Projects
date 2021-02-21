import random
randNumber = random.randint(1, 100)
guesses = 0
user_guess = None
while(user_guess != randNumber):
    user_guess = int(input("Enter your Guess: "))

    if user_guess == randNumber:
        print("Congratulations you guessed the number")
    else:
        print("You are wrong, ", end="")
        guesses += 1
        if user_guess < randNumber:
            print("Guess higher")
        elif user_guess > randNumber:
            print("Guess Lower")

print(f"You guessed the number in {guesses} number of guesses.")