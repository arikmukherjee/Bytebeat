def min_coins(amount, coins):
    num_coins = [float('inf')] * (amount + 1)
    num_coins[0] = 0
    used_coins = [[] for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and num_coins[i - coin] + 1 < num_coins[i]:
                num_coins[i] = num_coins[i - coin] + 1
                used_coins[i] = used_coins[i - coin] + [coin]

    return num_coins[amount], used_coins[amount]


def main():
    try:
        amount = int(input("Enter the amount: "))
        coin_list = input("Enter the coin denominations separated by spaces: ").split()
        coins = [int(coin) for coin in coin_list]

        min_coins_needed, denominations = min_coins(amount, coins)

        print("Minimum number of coins needed:", min_coins_needed)
        print("Denominations used:")
        for coin in set(denominations):
            count = denominations.count(coin)
            print(f"{count} coin(s) of denomination {coin} (Total: {count * coin})")

    except ValueError:
        print("Please enter valid integers for amount and coin denominations.")


if __name__ == "__main__":
    main()
