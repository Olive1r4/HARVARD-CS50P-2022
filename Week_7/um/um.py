import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matchs = re.findall(r"\bum", s, re.IGNORECASE)
    if matchs:
        print(matchs)
        return len(matchs)
    else:
        return 0

if __name__ == "__main__":
    main()