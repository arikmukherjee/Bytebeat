def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")
    
# Example usage:
p = list(map(int,input("dinensions of matrices :").split()))  # dimensions of matrices
m, s = matrix_chain_order(p)
print("Minimum number of scalar multiplications:", m[1][len(p) - 1])
print("Optimal parenthesization:", end=" ")
print_optimal_parens(s, 1, len(p) - 1)

print("\n")
for a in m:
    print(a)
print("\n")
for f in s:
    print(f)