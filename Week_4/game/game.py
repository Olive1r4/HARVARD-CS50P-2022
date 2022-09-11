# Import a random module
import random

def main():

    level = numLevel()
    guess = numGuess()

    while True:
        if guess < level:
            print("Too small!")
            guess = numGuess()
        elif guess > level:
            print("Too large!")
            guess = numGuess()
        else:
            print("Just right!")
            break
    exit()

# Function Return an integer between 1 and N
def numLevel():
    while True:
        try:
            n = int(input("Level: "))

            if n >= 1:
                # Return an integer between 1 and N
                return random.randint(1, n)

        # Check if the user input is an integer
        except ValueError:
            pass
# Function check if the user input is an integer and return an integer
def numGuess():
    while True:
        try:
            n = int(input("Guess: "))

            if n >= 1:
                return n
        # Check if the user input is an integer
        except ValueError:
            pass

main()