def main():
    x = int(input("What's X? "))
    print("x square is", square(x))

def square(n):
    return pow(n, 2)

main()