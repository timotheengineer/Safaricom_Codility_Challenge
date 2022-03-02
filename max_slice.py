def solution(A):

    sum_of_slices_list = [] #initialise sum list
    no_non_negative_slices_in_array = True #when slices are negative
    previous_index_of_negative_number = -1 # assuming the first index is negative

    for index , element in enumerate(A):#returns element and the index we start from 0 index

        if element < 0:
            
            if previous_index_of_negative_number == -1 and index == 0: 
                 # the first element is negative and thus no calculations is possible , just need to skip to next element
                previous_index_of_negative_number = 0
            else:
                slice_of_elements_to_calculate_sum = A[ (previous_index_of_negative_number + 1) : index] 
                sum_of_slices_list.append(sum(slice_of_elements_to_calculate_sum))
                previous_index_of_negative_number = index

        else: 
            no_non_negative_slices_in_array = False #where all elements are positive
            sum_of_slices_list.append(element)

    if no_non_negative_slices_in_array:
        return -1 
    else:
        return max(sum_of_slices_list)