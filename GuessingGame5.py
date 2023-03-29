import random


def main():
    NUM = random.randint(0, 10)
    GUESSES = 3

    guessCount = 0
    userGuess = int(input("Enter your guess (0-10): "))

    while guessCount != GUESSES:  # while loop iterates four times...
        if userGuess < NUM:
            guessCount += 1
            print("Incorrect guess, the number is higher.")
            userGuess = int(input("Enter your guess (0-10): "))
        elif userGuess > NUM:
            guessCount += 1
            print("Incorrect guess, the number is lower.")
            userGuess = int(input("Enter your guess (0-10): "))
        else:
            print("Congratulations, you guessed the number")
            break

    print("Game over - The number was " + str(NUM))


main()
