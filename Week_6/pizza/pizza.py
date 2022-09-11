import sys
import csv
from tabulate import tabulate

def main():
    # Pass the second argument (1:) to the function
    args = argv_check(sys.argv[1:])
    file_exist = is_exist_file(args[0])
    is_list = list_of_dict(file_exist)
    print(tabulate(is_list, headers="keys", tablefmt="grid"))

# Function to check if the arguments are valid
def argv_check(arg):
    # Check if the user passed an argument
    if len(arg) < 1:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 1:
        sys.exit("Too many command-line arguments")
    else:
        return arg

def is_csv(f):
    # Check if the file is a CSV file
    if not f.endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        pass

# Function to check if the file exists
def is_exist_file(arg):
    # Check if the file exists
    try:
        file = open(arg)
        # Check if the file is a CSV file
        is_csv(arg)
    # If the file does not exist, catch the error and exit
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return file

# Function to create a list of dictionaries
def list_of_dict(file):
    # Create a list of dictionaries
    listDict = []
    # Read the file as a dictionary
    for row in csv.DictReader(file):
        # Append the dictionary to the list
        listDict.append(row)
    return listDict

if __name__ == "__main__":
    main()