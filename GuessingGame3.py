
# Pseudocode

# CONSTANTS
# NUM = 5
# GUESSES = 3
#
# inputs
# userGuess = "Enter your guess (0-10): "
#
# processing
# for count = GUESSES (?)
#   if userGuess is less than NUM:
#       output "Incorrect guess, the number is higher"
#       userGuess = "Enter your guess (0-10)"
#   elif userGuess is greater than NUM:
#       output "Incorrect guess, the number is lower"
#       userGuess = "Enter your guess (0-10)"
#   else (userGuess = NUM):
#       output "Congratulations, you guessed the number"
#
# output "Game over :( The number was..."

NUM = 5
GUESSES = 3

userGuess = int(input("Enter your guess (0-10): "))

for count in range(1, GUESSES):
    if userGuess < NUM:
        print("Incorrect guess, the number is higher.")
        userGuess = int(input("Enter your guess (0-10): "))
    elif userGuess > NUM:
        print("Incorrect guess, the number is lower.")
        userGuess = int(input("Enter your guess (0-10): "))
    else:
        print("Congratulations, you guess the number")

print("Game over - The number was " + str(NUM))

