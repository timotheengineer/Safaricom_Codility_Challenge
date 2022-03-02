# Safaricom_Codility_Challenge
## Algorithms and coding
* Question 1

>Write a function 
def solution(A,B) that given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation of the number A*B.
For example,given A=3 and B=7 the function should return 3, because the binary representation of A*B=3*7=21 is 10101and it contains three bits set to 1.
Assume that:
>* A and B are integers within the range [0..100,000,000]

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
 * Question 2
 
 >An array A consisting of N integers is given. A slice of that are a pair of integers(P,Q) such that 0<=P<=Q<N. A slice(P<,Q) of array A is called non-negative if all the elements A[p],A[P+1],..A[Q-1],A[Q] are non-negative. The sum of a slice(P,Q) of array A is the value A[P]+A[P+1]+...+A[Q-1]+A[Q].
 For example, the following array A:
 A[0]=1
 A[1]=2
 A[2]=-3
 A[3]=4
 A[4]=5
 A[5]=-6
 has non-negative slices(0,0),(1,1),(0,1),(3,3),(4,4) and (3,4). 
 The sum of slice (0,1) is A[0]+A[1]=1+2=3
 The sum of slice (3,4) is A[3]+A[4]=4+5=9
 The sum of slice (4,4) is A[4]=5
 Write a function:
 def solution(A)
 that, given an array A consisting of N integers returns the maximum sum of any non-negative slice in the array. The function should return -1 if there are no non-negative slices in the array
 
```
def solution(A):

    sum_of_slices_list = []
    no_non_negative_slices_in_array = True 
    previous_index_of_negative_number = -1 # need to add a 1 to create a slice 

    for index , element in enumerate(A):

        if element < 0:
            # calculate the sum from the previous_index_of_negative_number to this index 
            if previous_index_of_negative_number == -1 and index == 0:
                 # the first element is negative and thus no calculations is possible , just need to skip to next element
                previous_index_of_negative_number = 0
            else:
                slice_of_elements_to_calculate_sum = A[ (previous_index_of_negative_number + 1) : index] 
                sum_of_slices_list.append(sum(slice_of_elements_to_calculate_sum))
                previous_index_of_negative_number = index

        else: 
            no_non_negative_slices_in_array = False 
            sum_of_slices_list.append(element)

    if no_non_negative_slices_in_array:
        return -1 
    else:
        return max(sum_of_slices_list)
```
    
