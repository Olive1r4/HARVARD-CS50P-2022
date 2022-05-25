def main():
    mass = int(input("Mass: "))
    print(f"{einsten(mass)}")

def einsten(mass):
    return (mass * pow(300000000,2))
main()