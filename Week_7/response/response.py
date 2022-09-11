from validator_collection import validators, checkers, errors
def main():
    mail = input("What's your email address? ")
    if validade(mail):
        print("valid")
    else:
        print("invalid")

def validade(mail):
    try:
        email_address = validators.email(mail)
        if checkers.is_email(email_address):
            return True
    except errors.InvalidEmailError:
        return False
    except errors.EmptyValueError:
        return False
main()