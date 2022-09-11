def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    gauge(percentage)
    print(gauge(percentage))

def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])

    while True:
        try:
            f = x / y
            if f <= 1:
                return round(f * 100)
            else:
                fraction = input("Fraction: ").split("/")
                x = int(fraction[0])
                y = int(fraction[1])
        except (ValueError, ZeroDivisionError):
                raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
