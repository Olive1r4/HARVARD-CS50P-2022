def main():
    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # check length
    if len(s) < 3 or len(s) > 7:
        return False
    # check string is alphanumeric(letters and numbers)
    elif s.isalnum() == False:
        return False
    # check first and second character are letters
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    for i in range(len(s)):
        # search for the first number
        if s[i].isnumeric() == True:
            # divide string into two parts after the first number
            s = s[i:len(s)]
            if s[0] == '0':
                return False
            # check if second part is numbers
            elif s.isnumeric() == False:
                return False
            break
    return True
main()