def solution(A,B):
    multiple = A * B
    binary_literal = bin(multiple)
    binary_string = binary_literal.split('b')[-1]
    return binary_string.count("1")