import random

def countP(string: str) -> int:
    string.lower()
    return string.count("p")

def countvowels(string: str) -> int:
    count = 0
    vowels = "aeiouyåäö"
    for char in string:
        if char.lower in vowels:
            count += 1
    return count

def reversestr(string: str) -> None:
    revstring: str = ""
    for place in range(1, len(string)+1):
        revstring += string[-place]
    return revstring

def palendrometest(string: str) -> bool:
    reverse: str = reversestr(string)
    reverse = reverse.replace(" ", "")
    string = string.replace(" ", "")
    return (reverse == string)