def main():
    t = input("Greeting: ")
    greeting(t)

def greeting(t):
    t = t.lower().strip()
    #find() returns -1 if the substring is not found
    if t.find("hello") != -1:
        print("$0")
    elif t[0] == "h":
        print("$20")
    else:
        print("$100")
main()
