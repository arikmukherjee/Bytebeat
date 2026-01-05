import tokenize
import math

def count_operators_and_operands(file_path):
    with open(file_path, 'rb') as file:
        tokens = tokenize.tokenize(file.readline)
        operators = []
        operands = []
        
        for token in tokens:
            if token.type == tokenize.OP:
                operators.append(token.string)
            elif token.type == tokenize.NAME:
                operands.append(token.string)
        
    return operators, operands

def halsted_metric(N1,N2,n1,n2):
    N = N1 + N2

    N_cap = n1*math.log2(n1) + n2*math.log2(n2)
    print("Halsted Program Length: {:.2f}".format(N_cap))
    n = n1 + n2
    print("Halsted Vocabulary: ",n)
    V = N*math.log2(n)
    print("Halsted Volume: ",n)

def main():
    file_path = 'halsted_input.py'  # Replace with the path to your Python file
    operators,operands = count_operators_and_operands(file_path)

    print(operands)
    N1 = len(operators)
    N2 = len(operands)
    n1 = len(set(operators))
    n2 = len(set(operands))

    halsted_metric(N1,N2,n1,n2)

if __name__ == '__main__':
    main()