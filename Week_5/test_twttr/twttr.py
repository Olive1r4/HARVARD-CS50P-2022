def main():
    word = input("Input: ")
    print("Output:", shorten(word))

def shorten(word):
    short = ""
    for i in range(len(word)):
        if "AEIOUaeiou".find(word[i]) != -1:
            short += word[i].replace(word[i], "")
        else:
            short += word[i]
    return short

if __name__ == "__main__":
    main()
