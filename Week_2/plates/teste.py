def main():
    s = input("Input: ")
    if len(s) < 3 or len(s) > 7:
        print("a")
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        print("c")

    for i in range(len(s)):
        if s[i].isnumeric() == True:
            s = s[i:len(s)]
            print(s)
            if s[0] == "0":
                print("d")
            elif s[-1].isalpha() == True:
                print("e")
            break
    print("f")
main()