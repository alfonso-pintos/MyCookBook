import random

# game setup
print("Welcome to the guessing game!")
number_of_guesses = 3 # user has 3 guesses before losing game
user_won = False

# Computer guesses a random number between 1-10

correct_answer = random.randint(1, 10)


while number_of_guesses > 0:
    # user guesses number
    user_guess = input("Guess a number between 1 and 10: ")
    user_guess = int(user_guess)

    # computer tells user whether guess was too high or too low
    if user_guess == correct_answer:
        print("You guessed right!")
        user_won = True
        break
    elif user_guess > correct_answer:
        print("Too high!")
    elif user_guess < correct_answer:
        print("Too low!")

    number_of_guesses -= 1


if user_won == True:
    print("You won!")
else:
    print("You lost!")

