# This is the guessTheNumberGames::
name_of_the_game = "***GUESS-THE-NUMBER***"
print(name_of_the_game.center(100))
# Generate the actual number
import random
actualNumber = random.randint(1, 20)
print('I am thinking of a number between 1 to 20 ')

# Guesses by players
for guessTaken in range(6):
    print('Take a guess!!')
    guess = int(input())
    if guess > actualNumber:
        print('Your guess is too high. ')
    elif guess < actualNumber:
        print('Your guess is too low. ')
    else:
        break
# Winner
if guess == actualNumber:
    print('You guessed my number in ', guessTaken, 'guesses. ')
    print("Congratulation's")
else:
    print('Nope! the number i was of thinking was ', actualNumber)
    print('Better luck next time.')

