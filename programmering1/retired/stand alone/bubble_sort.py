import time, random

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
    

def list_validation(lst: list):
    if type(lst) != list:
        raise TypeError("the argument must be a list.")
    if len(lst) < 2:
        raise Exception("The list must have at least 2 elements.")
    for element in lst:
        if type(element) not in [int, float]:
            raise TypeError("All elements in the list must be integers or floats.")



def sorting(lst: list) -> list:
    # ta en lista av nummer, returnera en listan sorterad, mist till högst. 
    # use bubble sort.

    # validate input
    list_validation(lst)

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
    list_validation(input_list)
    
    # check if list is sorted
    if input_list == sorting(input_list.copy()):
        return True
    else:
        return False


def custom_sort(lst: list) -> list:
    even_part: list = []
    odd_part: list = []
    decimal_part: list = []

    list_validation(lst)

    for item in lst:
        if item%2 == 0:
            even_part.append(item)
        elif item%2 == 1:
            odd_part.append(item)
        else:
            decimal_part.append(item)
    
    lst = []

    for part in [even_part, odd_part, decimal_part]:
        if len(part) > 2:
            sorting(part)
            lst.extend(part)

    return lst



test_list = []

i = 0
element_num_list = []

for element_number in range(1000, 1801, 200):
    element_num_list.append(element_number)

for element_index in range(0, len(element_num_list)):
    i = 0
    test_list = []
    while i < element_num_list[element_index]:
        test_list.append(random.randint(-1000, 1000))
        i += 1


    start_time = time.perf_counter()

    sorted_list = sorting(test_list)

    end_time = time.perf_counter()

    time_taken = end_time - start_time

    sort_start = time.perf_counter()

    test_list.sort()

    sort_end = time.perf_counter()

    sort_time = sort_end - sort_start

    print(f"it took: {time_taken} (my sotring) vs {sort_time} (.sort) \n length: {element_num_list[element_index]} \n")