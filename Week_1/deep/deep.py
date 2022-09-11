def main():
    answer = input("What is the answer to life, the universe, and everything? ")
    answer_to_life(answer)

def answer_to_life(n):
    # remove spaces and transform to lower case
    n = n.lower().strip()
    if n == "42" or n == "forty-two" or n == "forty two":
        print("Yes")
    else:
        print("No")
main()