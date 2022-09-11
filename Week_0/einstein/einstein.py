def main():
    mass = int(input("Mass (in kilograms): "))
    print(f"{einstein(mass)}")

#function to calculate the force of gravity
def einstein(mass):
    mass = mass * pow(300000000,2)
    return mass
main()