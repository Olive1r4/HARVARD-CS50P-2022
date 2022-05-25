def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# function to convert dollars to float
def dollars_to_float(d):
    # remove $ and ,
    d = d.strip("$")
    d = float(d)
    return d

# function to convert percent to decimal
def percent_to_float(p):
    #remove %
    p = p.strip("%")
    p = float(p) / 100
    return p

main()