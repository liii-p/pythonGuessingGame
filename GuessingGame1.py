"""
This program will use a constant variable and require the user to guess what
number the variable is.
"""

# Pseudocode
# Program GuessingGame1

# CONSTANTS
# NUM = 5

# inputs
# output "Number guessing game"
# userGuess = output "Enter your guess (1-10):

# processing
# if userGuess = NUM:
#   output "Congratulations, you guessed the number."
# else:
#   output "No that's not correct, the number was...NUM"

NUM = 5

print("Number guessing game by Lianna Pyman")
userGuess = int(input("Enter your guess (1-10): "))

if userGuess == NUM:
    print("Congratulations, you guessed the number.")
else:
    print("No that's not correct, the number was " + str(NUM))


