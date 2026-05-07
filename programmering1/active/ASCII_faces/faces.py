"""
Projekt 4: ASCII-ansikten
Ett interaktivt program där användaren kan skapa, klustra och slumpa ASCII-ansikten.
"""

import random, json


# === FUNKTIONER FÖR ANSIKTEN ===

eyes = ["o", "-", "^", "x", "T", ">", "@"]
mouths = ["_", "o", "^", "x", "T"]
cheeks = ["()", "[]", "{}", "<>"]
json_url = "faces.json"

def skapa_ansikte(ogon: str, mun: str, ram: str):
    if ogon not in eyes:
        raise Exception("not valid eye")
    if mun not in mouths:
        raise Exception("not valid mouth")
    if ram not in cheeks:
        raise Exception("not valid cheek")
    
    return f"{ram[0]}{ogon}{mun}{ogon}{ram[1]}"


def slumpa_ansikte():

    picks = []
    for choice_list in [eyes, mouths, cheeks]:
        picks.append(random.choice(choice_list))

    return skapa_ansikte(picks[0],picks[1],picks[2])


# === FUNKTIONER FÖR KLUSTER ===

def skriv_ut_kluster(bredd: int, hojd: int, ansikte: str):
    if type(bredd) != int or type(hojd) != int:
        raise TypeError("bredd and hojd must be integers")
    if type(ansikte) != str:
        raise TypeError("ansikte must be a string")
    
    for row in range(hojd):
        for column in range(bredd):
            print(ansikte, end=" ")
        
        print("")


def skriv_ut_slumpkluster(bredd, hojd):
    if type(bredd) != int or type(hojd) != int:
        raise TypeError("bredd and hojd must be integers")
    
    for row in range(hojd):
        for column in range(bredd):
            print(slumpa_ansikte(), end=" ")
        
        print("")


def ask_something(subject, options: list):
    while True:
        print(f"you are picking the {subject}")
        print("these are your options, pick one: (pick by writing the option)")
        for option in options:
            print(option)
        
        pick = input("> ").lower()

        if pick in options: #type: ignore
            return pick
        else:
            print(f"that ({pick}) is not an option")


def width_and_height():
    print("what width do you want?")
    asking = True
    while asking:
        choice = input("> ")
        try:
            width = abs(int(choice))
            asking = False
        except ValueError:
            print("that is not an option, you must choose an integer")
    
    print("what height do you want?")
    asking = True
    while asking:
        choice = input("> ")
        try:
            height = abs(int(choice))
            asking = False
        except ValueError:
            print("that is not an option, you must choose an integer")
    
    return [width, height]

# === MENYFUNKTIONER ===


def skapa_eget_ansikte():
    print("you are creating your own face")
    eye = ask_something("eyes", eyes)
    mouth = ask_something("mouths", mouths)
    cheek = ask_something("cheeks", cheeks)
    return skapa_ansikte(eye, mouth, cheek)


def skapa_kluster():
    print("would you like to use an existing face or pick your own")

    asking = True
    while asking:
        choice = input("Y/N > ").upper()
        if choice in ["Y", "N"]:
            asking = False
        else:
            print("that is not an option")
    
    if choice == "Y":
        face = ask_something("face", ladda_ansikten_fran_json(json_url))
    
    else:
        face = skapa_eget_ansikte()
    
    width, height = width_and_height()

    skriv_ut_kluster(width, height, face)


def visa_slump_ansikte():
    print(slumpa_ansikte())


def visa_slumpkluster():
    width, height = width_and_height()
    skriv_ut_slumpkluster(width, height)


# === HUVUDPROGRAM ===

def huvudprogram():
    """Huvudprogrammet som styr menyn och programflödet."""
    while True:
        print("\n--- ASCII-ANSIKTEN ---")
        print("1. Skapa eget ansikte")
        print("2. Skapa kluster (samma ansikte)")
        print("3. Slumpa ett ansikte")
        print("4. Slumpa kluster (blandade ansikten)")
        print("5. Avsluta")
        
        val = input("Välj: ")
        
        if val == "1":
            face = skapa_eget_ansikte()
            spara_ansikte_till_json(face, json_url)
        elif val == "2":
            skapa_kluster()
        elif val == "3":
            visa_slump_ansikte()
        elif val == "4":
            visa_slumpkluster()
        elif val == "5":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def farglagg_ansikte(ansikte, farg_kod):
    """
    Lägger till ANSI-färgkoder runt ett ansikte.
    
    Parametrar:
        ansikte (str): Ansiktet som ska färgläggas
        farg_kod (str): ANSI-färgkod (t.ex. "\033[91m")
    
    Returnerar:
        str: Ansikte med färgkoder
    """
    # TODO: return farg_kod + ansikte + "\033[0m"
    pass


def spara_ansikte_till_json(ansikte, filnamn="faces.json"):
    data = ladda_ansikten_fran_json(filnamn)
    if ansikte not in data:
        data.append(ansikte)

        with open(filnamn, "w") as faces_file:
            json.dump(data, faces_file)


def ladda_ansikten_fran_json(filnamn="faces.json"):
    with open(filnamn, "r") as faces_file:
        faces = json.load(faces_file)
    return faces


# === TURTLE-UTMANING (FÖR DIG MED TURTLE) ===

def rita_ansikte_med_turtle(ogon, mun, ram):
    """
    EXTRA UTMANING: Ritar ett ansikte med Turtle-grafik istället för ASCII.
    Detta är för de som har tillgång till Turtle-biblioteket.
    """
    # TODO: Importera turtle
    # TODO: Skapa en turtle
    # TODO: Rita två cirklar som ögon
    # TODO: Rita en båge som mun
    # TODO: Rita en cirkel som huvud (ram)
    # TODO: turtle.done()
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()