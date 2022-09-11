def main():
    exp = input("Expression: ")
    print(float(f"{calculate(exp):.2f}"))

def calculate(exp):
    n = exp.split(" ")
    x = int(n[0])
    y = n[1]
    z = int(n[2])

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z
main()