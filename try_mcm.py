# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm

def mcm(p):
    """
    Function to find the optimal parenthesization of matrices using dynamic programming.

    Parameters:
    - p: List of matrix chain dimensions

    Returns:
    - s: Matrix storing split positions for optimal parenthesization
    """
    n = len(p) - 1  # Number of matrices
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Matrix to store the split positions
    
    # For a single matrix, split position is not relevant
    for i in range(1, n + 1):
        s[i][i] = i
    
    # L is the chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            for k in range(i, j):
                # Update the split position if a better parenthesization is found
                if s[i][j] == 0 or p[i - 1] * p[k] * p[j] < p[i - 1] * p[s[i][j]] * p[j]:
                    s[i][j] = k
    
    return s

def optimal_parens(s, i, j):
    """
    Recursive function to print the optimal parenthesization of matrices.

    Parameters:
    - s: Matrix storing split positions
    - i: Starting index
    - j: Ending index
    """
    if i == j:
        print(f'A{str(i)}', end='')
    else:
        print('(', end='')
        # Recursively print optimal parenthesization for left and right subproblems
        optimal_parens(s, i, s[i][j])
        optimal_parens(s, s[i][j] + 1, j)
        print(')', end='')

# User input
dimensions = list(map(int, input("Enter matrix chain dimensions as a list: ").split()))

# Find optimal parenthesization
s = mcm(dimensions)

# Print optimal parenthesization
print("Optimal parenthesization:", end=' ')
optimal_parens(s, 1, len(dimensions) - 1)
print("\n")
for a in s:
    print(a)