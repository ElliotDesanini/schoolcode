"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.

top 5
easy, medium, hard

object:
{
"namn": "str",
"gissningar": int,
"difficulty": "str"
}
"""

import random
import json
import os

# === FILHANTERING ===

def ladda_highscore(filnamn:str="highscore.json") -> list:
    if not os.path.exists(filnamn):
        print("this file does not exist")
        return []
    
    with open(filnamn, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except Exception:
            data = []
        return data


def spara_highscore(highscore_lista:list, filnamn:str="highscore.json"):
    if not os.path.exists(filnamn):
        print("this file does not exist")
        return []
    
    with open(filnamn, "w", encoding="utf-8") as file:
        json.dump(highscore_lista, file, indent=4, ensure_ascii=False)


def add_highscore(highscore:dict, filename:str="highscore.json"):
    data = ladda_highscore(filename)
    data.append(highscore)
    spara_highscore(data, filename)

def sortera_highscore(highscore_lista:list) -> list:
    sorted(highscore_lista, key=lambda element: element["gissningar"], reverse=True)
    return highscore_lista


def choose_difficulty(difficulties:list=["easy", "medium", "hard"]) -> str:
    while True:
        print("    choose a difficulty from the following:")
        print("write the name of the difficulty you want")
        for element in difficulties:
            print(f"{element}")
        
        choice = input("> ").strip().lower()

        for element in difficulties:
            if choice == element:
                return choice
            
        if choice not in difficulties:
            print("that is not a possible difficulty")

# === SPELMECKANIK ===

def spela_omgang(hidden_number_range:int=100):
    hidden_number = random.randint(1, hidden_number_range)
    guesses = 0

    while True:
        print(f"\ncurrent guesses made: {guesses}")
        print("what number do u think it is?")
        try:
            guessed_number = int(input(" >").strip())
        except Exception:
            print("that is not a valid input.")
    
        if guessed_number == hidden_number:
            guesses += 1
            print(f"that is correct, you guessed correctly after {guesses} guesses!")
            return guesses
        
        elif guessed_number < hidden_number:
            guesses += 1
            print(f"{guessed_number} is too low")
        
        else:
            guesses += 1
            print(f"{guessed_number} is too high")
    



    """
    Spelar en omgång av Högt/lågt.
    
    Returnerar:
        int: Antalet gissningar som behövdes för att gissa rätt
    """
    # TODO: Implementera funktionen
    # 1. Välj ett slumpmässigt tal mellan 1 och 100 med random.randint()
    # 2. Skapa en variabel för antal gissningar (börja på 0)
    # 3. Skapa en while-loop som fortsätter tills spelaren gissar rätt
    # 4. Inuti loopen: fråga efter gissning, öka räknaren, ge feedback (högt/lågt/rätt)
    # 5. När spelaren gissar rätt: returnera antalet gissningar
    pass


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
    """
    Visar highscore-listan sorterad med bästa spelaren först.
    
    Parametrar:
        highscore_lista (list): Listan som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Kontrollera om listan är tom först
    # Tips: Sortera med sorted() och key=lambda x: x["gissningar"]
    # Tips: Använd enumerate() för att numrera spelarna från 1
    pass


# === HUVUDPROGRAM ===

def huvudprogram():
    commands:list = ["see top 5 scores", "START GAME", "see all high scores", "quit"]

    menu_text:str = f"""
    the following are the menu options, input a number related to an action to continue.

"""
    for element in commands:
        menu_text += f"\n            {commands.index(element)}. {element}"

    game_on:bool = True

    difficulty_decider:dict = {
        "easy": 128,
        "medium": 258,
        "hard": 512
    }

    print("High Low \ni will pick a number, and you will guess it.")

    while game_on:
        print(menu_text)
        command = input("> ").strip()

        match command:
            case "0":
                highscore = ladda_highscore()
                for element in sortera_highscore(highscore)[:5]:
                    print(f"namn: {element["namn"]}; gissningar: {element["gissningar"]}")
                
            case "1":
                print("GAME STARTED!")
                difficulty = choose_difficulty(list(difficulty_decider.keys()))
                number_range = difficulty_decider[difficulty]
                guesses = spela_omgang(number_range)

                name_score = input("what would you like to be called?\n> ")

                highscore = {"namn": name_score, "gissningar": guesses}
                add_highscore(highscore)

            case "2":
                highscore = ladda_highscore()
                for element in sortera_highscore(highscore):
                    print(f"namn: {element["namn"]}; gissningar: {element["gissningar"]}")
            
            case "3":
                game_on = False
                print("have a good day.")
            
            case _:
                print("that is not a valid input")

    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda highscore med ladda_highscore()
    # 2. Skapa en while-loop som visar menyn
    # 3. Menyn ska ha alternativen:
    #    1. Spela ny omgång
    #    2. Visa highscore
    #    3. Avsluta
    # 4. Vid val 1:
    #    - Anropa spela_omgang() för att få antalet gissningar
    #    - Fråga efter spelarens namn
    #    - Skapa en dictionary {"namn": namn, "gissningar": antal}
    #    - Lägg till i highscore-listan
    #    - Spara med spara_highscore()
    # 5. Vid val 2: anropa visa_highscore()
    # 6. Vid val 3: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()