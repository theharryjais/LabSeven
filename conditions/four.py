import random
secret_number = random.randint(0, 11)
total_attempts = 3
no_of_attempts = 0
while no_of_attempts < 3:
    guessed_number = int(input("Guess the secret number between 1 and 10: "))
    if guessed_number != secret_number :
        print("That's not the secret number.")
        no_of_attempts += 1
        if no_of_attempts == 3:
            print("You loose.")

    else:
        print("You won!")
        break