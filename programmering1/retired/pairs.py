def pairs(element_list: list) -> list:
    pair_list: list = []
    for element1 in element_list:
        for element2 in element_list:
            pair_list.append(f"{element1}{element2}")
    return pair_list

for pair in pairs(["b", "f", "g", "h", "j", "k", "m", "n", "p", "r", "s", "t", "v", "w"]):
    print(pair, end=" ")