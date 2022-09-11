def main():
    print("Amount Due: 50")
    coin  = int(input("Insert Coin: "))
    coin = coin_check(coin)
    print(f"Change Owed: {change(coin) - 50}")

# check if coin is 25, 10, 5
def coin_check(coin):
    while coin != 25 and coin != 10 and coin != 5:
        print("Amount Due: 50")
        coin = int(input("Insert Coin: "))
    return coin

# calculate change owed
def change(coin):
    sum = 0
    while sum < 50:
        if coin == 25:
            sum += 25
        elif coin == 10:
            sum += 10
        elif coin == 5:
            sum += 5

        if sum < 50:
            print("Amount Due:", 50 - sum)
            coin = int(input("Insert Coin: "))
            coin = coin_check(coin)
        else:
            return sum
main()