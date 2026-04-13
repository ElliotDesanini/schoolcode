# functionality: read quotes, add quotes, read qoutes, remove quotes, edit qoutes, search by genre

"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""

import random
import os


def ladda_citat_fran_fil(filnamn: str) -> list:
    if not os.path.exists(filnamn):
        print("this file does not exist")
        return []

    with open(filnamn, "r", encoding="utf-8") as quotes_file:
        return quotes_file.readlines()


def spara_citat_till_fil(citatlista: list, filnamn: str) -> None:
    if not os.path.exists(filnamn):
        print("this file does not exist")
        return

    with open(filnamn, "w", encoding="utf-8") as quotes_file:
        quotes_file.writelines(citatlista)


def visa_alla_citat(citatlista):
    if type(citatlista) != list:
        print("that is not a valid list to show")
        return

    for index, quote in enumerate(citatlista):
        print(f"{index}: {quote.strip()}")


def lagg_till_citat(citatlista: list):
    print(
        "write your quote in the form:\n"
        "  quote - author\n"
        "if you did not inted this action, reply with something not following this format."
    )

    quote = input("> ").strip()

    if "-" not in quote:
        print("Incorrect Input\nyou are missing an author or you did not properly seperate your author form your quote.")
    elif quote.endswith("-"):
        print("Incorrect Input\nyour quote cannot end with '-', there must be an author")
    elif quote.count("-") > 1:
        print("Incorrect Input\nif there are multiple authors, seperate them with ','. do not use multiple '-'")
    else:
        citatlista.append(quote + f"\n")


def slumpa_citat(citatlista) -> str:
    if len(citatlista) == 0:
        print("the given list is empty")
        return ""
    else:
        return random.choice(citatlista).strip()


def choose_genre(genres: list) -> str:
    print("choose genre from: ")
    for genre in genres:
        print(genre)

    choosen = input("> ").strip()

    if choosen in genres:
        return choosen
    else:
        print("that is note an option.")
        return ""


def remove_quote(quotelist: list):
    visa_alla_citat(quotelist)
    print("what is the index of the quote you want to remove?")

    try:
        quote = int(input("> ").strip())
    except ValueError:
        print("that is not a valid number")
        return

    if quote in range(len(quotelist)):
        quotelist.pop(quote)
    else:
        print("quote does not exist")


def huvudprogram():
    running = True
    genres = ["programming", "motivational", "romance"]
    choosen_genre = ""
    quotes = []

    while running:
        print(f"""
        1 - see quotes

        2 - add quote

        3 - help

        4 - exit program

        5 - remove quote

        6 - see gernes

        7 - choose genre

        8 - exit genre

        9 - see random quotes

        current genre: {choosen_genre if choosen_genre != "" else 'none'}""")

        command = input("> ").strip()

        match command:
            case "1":
                if choosen_genre != "":
                    quotes = ladda_citat_fran_fil(f"quotes/{choosen_genre}.txt")
                    visa_alla_citat(quotes)
                else:
                    quotes = []
                    for genre in genres:
                        quotes.extend(ladda_citat_fran_fil(f"quotes/{genre}.txt"))
                    visa_alla_citat(quotes)

            case "2":
                if choosen_genre != "":
                    quotes = ladda_citat_fran_fil(f"quotes/{choosen_genre}.txt")
                    lagg_till_citat(quotes)
                    spara_citat_till_fil(quotes, f"quotes/{choosen_genre}.txt")
                else:
                    print("you must select a genre for your quote")
                    choosen_genre = choose_genre(genres)

                    if choosen_genre != "":
                        quotes = ladda_citat_fran_fil(f"quotes/{choosen_genre}.txt")
                        lagg_till_citat(quotes)
                        spara_citat_till_fil(quotes, f"quotes/{choosen_genre}.txt")

            case "3":
                print("there are 3 genres of qoutes: romace, programming, and motivational.\nyou can perform actions by inputing numbers and quotes")

            case "4":
                print("have a good day")
                running = False

            case "5":
                if choosen_genre == "":
                    print("you must choose a genre first")
                    choosen_genre = choose_genre(genres)

                if choosen_genre != "":
                    quotes = ladda_citat_fran_fil(f"quotes/{choosen_genre}.txt")
                    if quotes is not None:
                        remove_quote(quotes)
                        spara_citat_till_fil(quotes, f"quotes/{choosen_genre}.txt")

            case "6":
                for genre in genres:
                    print(genre)

            case "7":
                choosen_genre = choose_genre(genres)

            case "8":
                choosen_genre = ""

            case "9":
                if choosen_genre == "":
                    quotes = []
                    for genre in genres:
                        quotes.extend(ladda_citat_fran_fil(f"quotes/{genre}.txt"))
                else:
                    quotes = ladda_citat_fran_fil(f"quotes/{choosen_genre}.txt")

                print(slumpa_citat(quotes))

            case _:
                print("that is i not a valid command.")


if __name__ == "__main__":
    huvudprogram()