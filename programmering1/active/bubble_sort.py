def swap(input_list: list, index_1: int, index_2: int) -> list:
    # ta en lista och 2 index, byter plats på elemented med dessa index.

    # validate input
    if (index_1 >= len(input_list)) or (index_2 >= len(input_list)):
        raise IndexError("An index is out of bounds.")
    if type(input_list) != list:
        raise ValueError("The first argument must be a list")
    if len(input_list) < 2:
        raise Exception("The list must have at lest 2 elements")
    if type(index_1) != int or type(index_2) != int:
        raise TypeError("The indices, the second and third arguments, must be integers.")
    
    # swap elements
    swaped_list: list = input_list.copy()
    swaped_list[index_1] = input_list[index_2]
    swaped_list[index_2] = input_list[index_1]

    return swaped_list
    



def sorting(lst: list) -> list:
    # ta en lista av nummer, returnera en listan sorterad, mist till högst. 
    # use bubble sort.

    # validate input
    if type(lst) != list:
        raise TypeError("the argument must be a list.")
    if len(lst) < 2:
        raise Exception("The list must have at least 2 elements.")
    for element in lst:
        if type(element) not in [int, float]:
            raise TypeError("All elements in the list must be integers or floats.")
    
    # sort
    assesment_point = 0 # the index of the first element of the 2 elements being compaired
    end_point = len(lst) # index element where after we know they are in the right order
    loop_num = 0

    while True:
        loop_num += 1
        # swap if in wrong order
        if lst[assesment_point] > lst[assesment_point+1]:
            lst = swap(lst, assesment_point, assesment_point+1)
        assesment_point += 1

        # starts over when at the end of unsorted elements
        if assesment_point+1 == end_point:
            assesment_point = 0
            end_point -= 1

        # when everything except 1 has been sorted, we know it can only be in the right place
        if end_point == 1:
            return lst



def is_sorted(input_list: list) -> bool:
    # ta en lista, om == sorterad lista returnera True, annars False
    
    # validate input
    if type(input_list) != list:
        raise TypeError("the argument must be a list.")
    if len(input_list) < 2:
        raise Exception("The list must have at least 2 elements.")
    for element in input_list:
        if type(element) not in [int, float]:
            raise TypeError("All elements in the list must be integers or floats.")
    
    # check if list is sorted
    if input_list == sorting(input_list.copy()):
        return True
    else:
        return False





test_list: list = [1, 2.4, 3, 4, 3, 4, 5, 8, 5.32, 3, 1, 2.5, 145, 1, 32, 3.24]
sorted_list: list = [1,1.1,2,2.9,3,4,5,6,7,8,9,10]

print(sorting(test_list))
print(is_sorted(sorted_list))
print(is_sorted([2,3,1]))
