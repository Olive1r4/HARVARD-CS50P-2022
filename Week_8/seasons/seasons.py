from datetime import date
import inflect
import sys


def main():
    birth = input("Date of Birth: ")
    birthday = get_birthday_date(birth)
    minutes = get_minutes(birthday)
    words = convert_to_words(minutes)
    print(f"{words} minutes")


def get_birthday_date(birth):
    try:
        birthday = birth.split("-")
        dob = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
        if dob:
            return dob
    except ValueError:
        sys.exit("Invalid date")

def get_minutes(b):
    minuts = (date.today() - b).days * 24 * 60
    return minuts

def convert_to_words(m):
    p = inflect.engine()
    words = p.number_to_words(m, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
