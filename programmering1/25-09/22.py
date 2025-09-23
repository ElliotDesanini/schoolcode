import math
import random

def listoperations(list: list) -> None:
    print(f"basic {list}")
    print(f"index5 {list[5]}")
    print(f"index5: {list[5:]}")
    print(f"index:5 {list[:5]}")
    print(f"index5:12 {list[5:12]}")
    print(f".index18 {list.index(18)}")
    list.append(7)
    print(f".append7 {list}")
    print(f"len {len(list)}")
    print(f"sum {sum(list)}")
    print(f"max {max(list)}")
    print(f"min {min(list)}")
    print(f"sorted {sorted(list)}")
    list.sort(reverse=True)
    print(f"reverse {list}")
    list.sort(reverse=False)
    print(f".pop {list.pop()}")
    print(f".copy {list.copy()}")
    print(f".pop4 {list.pop(4)}")
    list.extend([1,2,3])
    print(f".extend[1,2,3] {list}")
    list.insert(3, 25)
    print(f".insert3,25 {list}")
    list.remove(4)
    print(f".remove4 {list}")
    list.clear()
    print(f".clear {list}")

test_list:list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def sort_even_and_odd(list: list) -> list:
    even = []
    odd = []
    for element in list:
        if not (element % 2):
            even.append(element)
        else:
            odd.append(element)
    return [even, odd]

def choose_lotto(list: list, length: int) -> list:
    lotto = []
    while True:
        lotto.append(list.pop(random.randint(1,len(list))))
        if len(lotto) == length:
            return lotto

def list_interact(list: list) -> None:
    choose_text:str = """

    Vad vill du göra?
    1. Titta på hela listan             2. Titta på ett givet läge i listan
    3. Lägga till ett värde i listan    4. Radera värdet på ett givet läge i listan
    5. Sortera listan                   6. Beräkna listans medelvärde
    7. Avsluta

    """
    avsluta = False
    while not avsluta:
        print(choose_text)
        command = input("what would you like to do? > ")
        match command:
            case "1":
                print(list)
            case "2":
                command = int(input("which? > "))
                print(list[command])
            case "3":
                command = int(input("which? > "))
                list.append(command)
                print(list)
            case "4":
                command = int(input("which? > "))
                list.remove(command)
                print(list)
            case "5":
                list.sort()
                print(list)
            case "6":
                medel = sum(list)/len(list)
                print(medel)
            case "7":
                avsluta = True
            case _:
                print("sorry that is not a valid input")

list_interact(test_list)