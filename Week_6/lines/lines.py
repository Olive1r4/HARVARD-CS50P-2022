import sys

def main():
    args = sys.argv[1:]
    argv_check(args)
    is_python_file(args)
    args = check_file(args)
    lines = lines_count(args)
    print(lines)


def argv_check(argument):
    # Check if the user passed an argument
    if len(argument) < 1:
        sys.exit("Too few command-line arguments")
    elif len(argument) > 1:
        sys.exit("Too many command-line arguments")
    else:
        return argument

def is_python_file(argument):
    # Check if the file is a Python file
    if not argument[0].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        return argument[0]

def check_file(argument):
    # Check if the file exists
    try:
        file = open(argument[0])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return file

def lines_count(file):
    # Count the number of lines in the file
    count = 0
    for row in file:
        if row.strip().startswith("#")  or row.strip() == "":
            pass
        else:
            count += 1
    return count

if __name__ == "__main__":
    main()