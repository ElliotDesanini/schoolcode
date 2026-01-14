import random
import math

def cel_to_far(cel : float) -> float:
    return ((cel*9/5) + 32)

def far_to_cel(far : float) -> float:
    return (far-32)*5/9

def high_or_lower(guesses : int) -> list:
    print(f"I will now pick a random number, you will try to guess within {guesses} guesses and i will tell you if it is higher or lower for each guess.")
    iteration = 0
    number = random.randint(1, 2000)
    while iteration <= guesses:
        while True:
            try:
                user_guess = int(input("your guess > "))
                break
            except Exception:
                print("\nthat did not work, please try again in another way\n")
        if user_guess > number:
            print(f"you have {guesses-(iteration)} left\n", "my number is lower\n")
        elif user_guess < number:
            print(f"you have {guesses-(iteration)} left\n", "my number is higher\n")
        else:
            return [iteration+1, True]
        iteration += 1
    return [guesses, False]


def factorial(number : int) -> int:
    return math.factorial(number)

def factorial2(number : int) -> int:
    answer = 1
    for i in range(1, number+1):
        answer *= i
    return answer

def sqrt_2(number : float, precition : int) -> float:
    side1 = number/2
    side2 = 2
    while True:
        if round(side1, precition) == round(side2, precition):
            return side1
        else:
            average = (side1 + side2)/2
            side1 = number/average
            side2 = average

def is_prime(number : int) -> bool:
    for i in range(2,(number/2)+1):
        if number%i == 0:
            return False
    return True