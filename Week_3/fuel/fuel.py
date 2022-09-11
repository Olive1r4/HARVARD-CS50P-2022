def main():
    fraction = get_fraction()

    if fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction}%")

def get_fraction():
    while True:
        # teste se o valor é enteiro
        try:
            f = input("Fraction: ").split("/")
            x = int(f[0])
            y = int(f[1])
            if x <= y:
                return int(round(x/y, 2)*100)
        # if user input is not an integer or fraction
        except (ValueError, ZeroDivisionError):
            # print error message or use pass
            pass
main()