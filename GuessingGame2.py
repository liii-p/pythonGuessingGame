
# Pseudocode
# Program GuessingGame2
#
# CONSTANTS
# NUM = 5

# inputs
# output "Number guessing game"
# userGuess = output "Enter your guess (1-10):

# processing
# if userGuess < NUM:
#   output "No, the number was higher, the number was..."
# elif userGuess > NUM:
#   output "No the number was lower, the number was..."
# else:
#   output "Congratulations, you guessed the number."

NUM = 5

print("Number guessing game by Lianna Pyman")
userGuess = int(input("Enter your guess (1-10): "))

if userGuess < NUM:
    print("No, the number was higher, the number was " + str(NUM))
elif userGuess > NUM:
    print("No, the number was lower, the number was " + str(NUM))
else:
    print("Congratulations, you guessed the number.")
