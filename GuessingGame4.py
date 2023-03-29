
# Pseudocode
#
# Program GuessingGame4
#
# CONSTANTS
# NUM = 5
# GUESSES = 3
#
# inputs
# guessCount = 0
# userGuess = "Enter your guess (0-10): "
#
# processing
#  while guessCount does not equal GUESSES:
#   if userGuess is less than NUM:
#       guessCount += 1
#       output "Incorrect guess, the number is higher"
#       userGuess = "Enter your guess (0-10)"
#   elif userGuess is greater than NUM:
#       guessCount += 1
#       output "Incorrect guess, the number is lower"
#       userGuess = "Enter your guess (0-10)"
#   else (userGuess = NUM):
#       output "Congratulations, you guessed the number"
#
# print("Game over - The number was..."

NUM = 5
GUESSES = 3

guessCount = 0
userGuess = int(input("Enter your guess (0-10): "))

while guessCount != GUESSES:
    if userGuess < NUM:
        guessCount += 1
        print("Incorrect guess, the number is higher.")
        userGuess = int(input("Enter your guess (0-10): "))
    elif userGuess > NUM:
        guessCount += 1
        print("Incorrect guess, the number is lower.")
        userGuess = int(input("Enter your guess (0-10): "))
    else:
        print("Congratulations, you guess the number")

print("Game over - The number was " + str(NUM))
