def coin_change(coins, amount):
    # Sort coins in descending order
    coins.sort(reverse=True)
    # Initialize dictionary to store the count of each coin
    coin_count = {}

    # Iterate through each coin denomination
    for coin in coins:
        # Calculate how many of this coin denomination can be used
        count = amount // coin
        # Update the remaining amount
        amount -= count * coin
        # Store the count of this coin denomination
        coin_count[coin] = count

    # If there is still some amount left, it means the greedy algorithm couldn't make change
    if amount != 0:
        print("Change cannot be made with the given coins.")
        return

    # Print the coins used and their counts
    print("Coins used to make change:")
    for coin, count in coin_count.items():
        print(f"{count} coins of {coin}")

if __name__ == "__main__":
    coins = list(map(int, input("Enter the denominations of coins separated by space: ").split()))
    amount = int(input("Enter the amount for which you want to make change: "))
    coin_change(coins, amount)
