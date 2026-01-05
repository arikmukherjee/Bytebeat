def matrix_chain_multiplication(p):
    """
    Function to find the optimal parenthesization of matrices using dynamic programming.

    Parameters:
    - p: List of matrix chain dimensions

    Returns:
    - m: Matrix storing minimum scalar multiplications
    - s: Matrix storing split positions for optimal parenthesization
    """
    n = len(p) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]  # Matrix to store the cost of scalar multiplications
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Matrix to store the split positions
    
    # For a single matrix, cost is zero
    for i in range(1, n + 1):
        m[i][i] = 0
    
    # L is the chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')  # Initializing to infinity
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m, s

def print_optimal_parens(s, i, j):
    """
    Recursive function to print the optimal parenthesization of matrices.

    Parameters:
    - s: Matrix storing split positions
    - i: Starting index
    - j: Ending index
    """
    if i == j:
        print(f'M{str(i)}', end='')
    else:
        print('(', end='')
        # Recursively print optimal parenthesization for left and right subproblems
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end='')

def print_binary_table(s):
    """
    Function to print the binary table representing split positions.

    Parameters:
    - s: Matrix storing split positions
    """
    n = len(s) - 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{s[i][j]:2}', end=' ')
        print()

def print_cost_table(m):
    """
    Function to print the cost table representing the minimum number of scalar multiplications.

    Parameters:
    - m: Matrix storing minimum scalar multiplications
    """
    n = len(m) - 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{m[i][j]:5}', end=' ')
        print()

# User input
dimensions = list(map(int, input("Enter matrix chain dimensions as a list: ").split()))

# Find optimal parenthesization and minimum scalar multiplications
m, s = matrix_chain_multiplication(dimensions)

# Print optimal parenthesization
print("Optimal parenthesization:", end=' ')
print_optimal_parens(s, 1, len(dimensions) - 1)

# Print binary table
print("\nBinary Table:")
print_binary_table(s)

# Print cost table
print("\nCost Table:")
print_cost_table(m)