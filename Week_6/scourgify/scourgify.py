import sys
import csv

def main():
    command_line_arguments()

    # Open the files
    students = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                students.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read file")

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)
            
# Check if the user pass two valid arguments
def command_line_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        pass
main()