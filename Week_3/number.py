def main():
    try:
        x = int(input("Please enter an integer: "))
        print(f"x is {x}")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
main()
#----------------------------------------------------------------------------------------------------------------------
def main():
    try:
        x = int(input("Please enter an integer: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print(f"x is {x}")
main()
#----------------------------------------------------------------------------------------------------------------------
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Please enter an integer: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        else:
            break
        return x
main()
#----------------------------------------------------------------------------------------------------------------------
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Please enter an integer: "))
        except ValueError:
            pass
main()
#----------------------------------------------------------------------------------------------------------------------
def main():
    x = get_int( "Wha's is x?" )
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()