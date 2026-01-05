def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a table to store lengths of LCSs
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Building the lcs_table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # LCS is last entry in the table
    lcs_length = lcs_table[m][n]

    # Constructing the LCS string itself
    lcs_string = [''] * (lcs_length + 1)
    lcs_string[lcs_length] = ''

    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_string[lcs_length - 1] = s1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Printing the length of LCS
    print("Length of Longest Common Subsequence:", lcs_table[m][n])

    # Printing the LCS table
    print("LCS Table:")
    for row in lcs_table:
        print(row)

    return ''.join(lcs_string)


# Get user input for the strings
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Compute and print the longest common subsequence
print("Longest Common Subsequence:", longest_common_subsequence(s1, s2))
