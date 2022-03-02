def solution(A,B):
    product = A * B

    binary_value_list = []
    dividend = product 
    quotient = -1

    while quotient != 0:
        quotient = dividend // 2
        remainder = dividend % 2
        binary_value_list.append(remainder)
        dividend = quotient 

    return binary_value_list.count(1)