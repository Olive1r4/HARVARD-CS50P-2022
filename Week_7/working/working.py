import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        input = re.search(r"^(0?[1-9]|1[0-2])(?::)?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2])(?::)?([0-6][0-6])? (AM|PM)$", s, re.IGNORECASE)
        if input:
            group1 = int(input.group(1))
            group2 = input.group(2)
            group4 = int(input.group(4))
            group5 = input.group(5)

            if input.group(3).upper() == "PM":
                if group1 < 12:
                    group1 += 12
                    group1 = str(group1)
            elif input.group(3).upper() == "AM":
                if group1 == 12:
                    group1 = "00"

            if input.group(6).upper() == "PM":
                if group4 < 12:
                    group4 += 12
                    group4 = str(group4)
            elif input.group(6).upper() == "AM":
                if group4 == 12:
                    group4 = "00"


            if input.group(2) == None:
                group2 = "00"
            if input.group(5) == None:
                group5 = "00"

            return (f"{group1:02}:{group2} to {group4:02}:{group5}")
        else:
            raise ValueError
    except ValueError:
        raise
if __name__ == "__main__":
    main()
