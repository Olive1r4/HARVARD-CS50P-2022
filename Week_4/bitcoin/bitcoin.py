import sys
import requests

def main():
    args = command_line_args()
    # Get the API  JASON from url
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Convert the JSON to a dictionary
    coin_list = response.json()
    # Get the value of the key "bpi"
    bitcoin_price = coin_list["bpi"]["USD"]["rate_float"]

    buy_price = bitcoin_price * args
    # Print the result with 4 decimal places and using "," as a separator thousands
    print(f"${buy_price:,.4f}")

# Function to get the command line arguments
def command_line_args():
    while True:
        try:
            # Get the command line arguments
            # If the user input nothing, return a message and exit the program
            if len(sys.argv) == 1:
                sys.exit("Missing command-line argument ")
            else:
                # If user input an argument
                len(sys.argv) == 2
                # try to convert the argument to a float
                args = float(sys.argv[1])
                return args

        except ValueError:
            # If the user input cant be converted to a float, return a message and exit the program
            sys.exit("Command-line argument is not a number")
main()