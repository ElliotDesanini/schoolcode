import turtle

# === FIGURER ===

def regular_shape(t, sidor, sida, farg):
    if (type(sidor) != int) or (type(sida) not in [float, int]) or (type(farg) != str):
        raise ValueError
    
    if sidor < 3:
        raise Exception("sidor cannot be less than 3")


    t.pencolor(farg)

    for i in range(sidor):
        t.forward(sida)
        t.left(360 / sidor)

def rita_kvadrat(t, sida, farg):
    regular_shape(t, 4, sida, farg)
    


def rita_triangel(t, sida, farg):
    regular_shape(t, 3, sida, farg)


def rita_cirkel(t, radie, farg):
    t.pencolor(farg)
    t.circle(radie)


def rita_blomma(t, kronblad, sida, farg):
    
    t.pencolor(farg)
    vinkel = 360 / kronblad

    for i in range(kronblad):
        rita_kvadrat(t, sida, farg)
        t.left(vinkel)

def get_speed(speeds : dict):
    while True:
        print("pick a speed")

        for key in speeds.keys():
            print(f"{key} : {speeds[key]}")
        
        picked_speed = input("> ")

        if picked_speed in speeds.keys():
            return speeds[picked_speed]
        else:
            print("that is not an option")



def ask_something(subject, options: list):
    while True:
        print(f"you are picking the {subject}")
        print("these are your options, pick one: (pick by writing the name of the option)")
        for option in options:
            print(option)
        
        pick = input("> ").lower()

        if pick in options: #type: ignore
            return pick
        else:
            print(f"that ({pick}) is not an option")

# === HUVUDPROGRAM ===

def huvudprogram():
    t = turtle.Turtle()
    
    speeds = {
        "medel" : 5,
        "snabb" : 7,
        "snabbast" : 0
    }

    sidoval = ["5", "10", "15", "20", "30", "40", "50", "100"]
    fargval = ["red", "blue", "yellow", "green"]
    hållval = ["left", "right", "forward", "backward"]

    t.speed(get_speed(speeds))
    
    while True:
        print("""\n--- TURTLE MÖNSTER ---
        1. Rita kvadrat
        2. Rita triangel
        3. Rita cirkel
        4. Rita blomma
        5. Sudda allt
        6. Gå fram/bak/vänster/höger
        7. Avsluta""")
        
        val = input("Valj: ")
        
        if val == "1":
            sida = int(ask_something("len of sides",sidoval))
            farg = ask_something("color",fargval)
            rita_kvadrat(t, sida, farg)
             
        elif val == "2":
            sida = int(ask_something("len of sides",sidoval))
            farg = ask_something("color", fargval)
            rita_triangel(t, sida, farg)
             
        elif val == "3":
            radie = int(ask_something("radius of the circle",sidoval))
            farg = ask_something("color", fargval)
            rita_cirkel(t, radie, farg)
             
        elif val == "4":
            sida = int(ask_something("len of side of leaves",sidoval))
            farg = ask_something("color", fargval)
            kronblad = int(ask_something("number of leaves", sidoval))
            rita_blomma(t, kronblad, sida, farg)

        elif val == "5":
            turtle.clear()

        elif val == "6":
            håll = ask_something("direction", hållval)
            walk = int(ask_something("len of walk",sidoval))

            if håll == "forward":
                t.forward(walk)
            elif håll == "backward":
                t.left(180)
                t.forward(walk)
            elif håll == "left":
                t.left(90)
                t.forward(walk)
            elif håll == "right":
                t.right(90)
                t.forward(walk)
        
        elif val == "7":
            turtle.done()
            break

        else:
            print("Ogiltigt val, forsok igen.")


if __name__ == "__main__":
    huvudprogram()