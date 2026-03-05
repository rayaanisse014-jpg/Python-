# Guessing game
#
# The secret number is 7. The user has three chances to guess it. Use a while
# loop to manage the turns.

# KEEP THE FOLLOWING STATEMENT UNCHANGED
secret_number = 7
max_attempts = 3

# Set up attempt counter, initially zero, and a boolean flag to remember if the current
# guess is correct, initially false.
attempts = 0
correct = False

while attempts < max_attempts and not correct:
    # Get current guess from standard input
    guess = int(input('Guess the number (0 to 9): '))
    
    # Evaluate the guess and print a message
    if guess == secret_number:
        print('You guessed correctly.')
        correct = True
    elif guess < secret_number:
        print('Too low.')
    else:
        print('Too high.')
    
    # Increment attempt counter
    attempts += 1

# After loop, display message if all attempts used up
if not correct:
    print('You have used all of your guesses.')