def main():
    name = input("camelCase: ")
    snake_case(name)

def snake_case(name):
    print("snake_case: ", end="")
    for i in range(len(name)):
        if name[i].islower():
            print(f"{name[i]}", end="")
        else:
            print(f"_{name[i].lower()}", end="")
    print()
main()
#------------------------------------------------
"""
# Other ways to do it:
def main():
    name = input("camelCase: ")
    print(f"snake_case: {snake_case(name)}")

def snake_case(name):
    n = ""
    for i in range(len(name)):
        if name[i].islower():
            n = n + name[i]
        else:
            n = n + "_" + name[i].lower()
    return n
main()
"""