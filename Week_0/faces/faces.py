def main():
    msg = input()
    print(msg_replace(msg))

def msg_replace(msg):
    msg1 = msg.replace(":)", "🙂")
    msg2 = msg1.replace(":(", "🙁")
    return msg2
main()
