# Funcoes também podem ser usadas no inputs
# name = input("What is your name? ").title().strip()
name = input("What is your name? ")

# strip() removes whitespace from the beginning and end of a string
# the strip() method returns a copy of the string with the leading and trailing

print(f"hello {name.strip().title()}!")