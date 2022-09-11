def main():
    text = input("Input: ")
    print(f"Output: {short_text(text)}")

def short_text(text):
    short = ""
    for i in range(len(text)):
        #  try to find A, E, I, O, U or a, e, i, o, u in the text
        if "AEIOUaeiou".find(text[i]) != -1:
            # if found, replace it with an empty string
            short += text[i].replace(text[i], "")
        else:
            # if not found, add it to the short string
            short += text[i]
    return short
main()