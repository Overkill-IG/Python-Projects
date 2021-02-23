import random
randNumber = random.randint(1, 100)
guesses = 0
user_guess = None
try:
    while(user_guess != randNumber):
        user_guess = int(input("Enter your Guess: "))

        if user_guess == randNumber:
           print(f"Congratulations you guessed the number, the number was '{randNumber}'")
        else:
           print("You are wrong, ", end="")
           guesses += 1
           if user_guess < randNumber:
               print("Guess higher")
           elif user_guess > randNumber:
               print("Guess Lower")

    print(f"You guessed the number in {guesses} number of guesses.")
except ValueError  as e:
    print("Please enter a valid value")
    print(f"Error: {e}")
