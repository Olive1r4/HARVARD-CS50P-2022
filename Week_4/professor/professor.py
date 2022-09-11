import random

def main():
    level = get_level()
    score = get_game(level)
    print(f"Score: {score}")

# Get level of game
def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            pass
    return level

# Generate random integer for the value of x and y
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

# Verify if the user input is correct result of x+y
# After 3 rounds, the game will show the correct result
def get_round(x, y):
    count_erro = 1
    while count_erro <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                erro += 1
                print("EEE")
        except:
            count_erro += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

# Count the score and the rounds(10 in this case)
def get_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
            x, y = generate_integer(level)
            r = get_round(x, y)
            if r == True:
                score += 1
            count_round += 1
    return score

if __name__ == "__main__":
    main()