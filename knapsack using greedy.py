def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    # Calculate the value-to-weight ratios for each item
    value_per_weight = [(values[i] / weights[i], i) for i in range(n)]
    # Sort items by their value-to-weight ratio in descending order
    value_per_weight.sort(reverse=True)

    total_value = 0
    selected_items = [0] * n

    knapsack_table = []

    for ratio, i in value_per_weight:
        if weights[i] <= capacity:
            selected_items[i] = 1
            total_value += values[i]
            capacity -= weights[i]
            knapsack_table.append([weights[i], values[i], selected_items[:]])

    return total_value, selected_items, knapsack_table

def display_table(table):
    headers = ["Weight", "Value", "Selected Items"]
    print("Greedy Knapsack Table:")
    print("  ".join(headers))
    for row in table:
        print("  ".join(map(str, row)))

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
    values = list(map(int, input("Enter the values of the items separated by space: ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value, selected_items, knapsack_table = knapsack_greedy(weights, values, capacity)

    print()
    display_table(knapsack_table)
    print("\nTotal value:", max_value)
    print("Selected items:", selected_items)
