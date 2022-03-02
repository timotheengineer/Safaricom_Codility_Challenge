# Safaricom_Codility_Challenge
## Algorithms and coding
* Question 1

Write a function 
def solution(A,B) that given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation of the number A*B.
For example,given A=3 and B=7 the function should return 3, because the binary representation of A*B=3*7=21 is 10101and it contains three bits set to 1.
Assume that:
* A and B are integers within the range [0..100,000,000]

## First approach
```
def solution(A,B):
    multiple = A * B
    binary_literal = bin(multiple)
    binary_string = binary_literal.split('b')[-1]
    return binary_string.count("1")
```
## Second Approach
```
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
    ```
