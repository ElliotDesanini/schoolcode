def bin_search(ordered_list: list, searching_item: int, start_index, end_index):
    iterations = 0
    print(f"searching for {searching_item} in {ordered_list}")
    while end_index >= start_index:
        mid_index = (start_index+end_index)//2
        if ordered_list[mid_index] == searching_item:
            print(f"{searching_item} found \n index: {mid_index} \n interations: {iterations}")
            return mid_index
        elif ordered_list[mid_index] > searching_item:
            iterations += 1
            end_index = mid_index
            print(f"upper half removed {ordered_list[start_index:end_index]}")
        else:
            iterations += 1
            start_index = mid_index+1
            print(f"lower half removed {ordered_list[start_index:end_index]}")
        
        if start_index == end_index:
            print(f"{searching_item} not in {ordered_list}")
            return None

# pga att varje steg alltid delar listan i 2
# så är den maximala mängden steg (om sökemålet hittas) är floor(log2(listans längd))