#0-1 knapsack using dp by SUBHAJIT KIRTANIA

def knapsack_01(weights, values, capacity):
    # Number of items
    n = len(weights)
    
    # Initialize a 2D array for dynamic programming
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the dynamic programming table using bottom-up approach
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the current item in the knapsack
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Exclude the current item from the knapsack
                dp[i][w] = dp[i - 1][w]

    # Return the dynamic programming table
    return dp

def print_table(dp):
    # Print the dynamic programming table
    for row in dp:
        print(row)

def main():
    # Take user input for the number of items, weights, values, and knapsack capacity
    n = int(input("Enter the number of items: "))
    weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
    values = list(map(int, input("Enter the values of the items separated by space: ").split()))
    capacity = int(input("Enter the knapsack capacity: "))

    # Compute the dynamic programming table
    dp_table = knapsack_01(weights, values, capacity)

    # Print the dynamic programming table
    print("Dynamic Programming Table:")
    print_table(dp_table)

    # Print the maximum value that can be obtained
    max_value = dp_table[n][capacity]
    print("The maximum value that can be obtained is:", max_value)

if __name__ == "__main__":
    main()
