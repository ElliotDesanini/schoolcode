# stats: str, dex, con

import json

monster_list: list = []
avatar_list: list = []


class Avatar:

    def __init__(self, id, strength: float = 1.0, dexterity: float = 1.0, constitution: float = 1.0):
        self.id = id
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

        monster_list.append(self.__dict__)

    def get_attack(self):
        attack = self.strength + (self.dexterity/2)
        return attack

    def get_defence(self):
        defence = self.constitution + (self.dexterity/2)
        return defence
    
    def __str__(self):
        return (
f"""
    -- {self.id} --
strength:       {self.strength}
dexterity:      {self.dexterity}
constitution:   {self.constitution}
"""
        )



class Monster:

    def __init__(self, id, strength: float = 1.0, dexterity: float = 1.0, constitution: float = 1.0):
        self.id = id
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

        monster_list.append(self.__dict__)

    def get_attack(self):
        attack = self.strength + (self.dexterity/2)
        return attack

    def get_defence(self):
        defence = self.constitution + (self.dexterity/2)
        return defence
    
    def __str__(self):
        return (
f"""
    -- {self.id} --
strength:       {self.strength}
dexterity:      {self.dexterity}
constitution:   {self.constitution}

attack:         {self.get_attack()}
defence:        {self.get_defence()}
"""
        )




def save_creature(creature: str, is_monster: bool):
    if is_monster:
        filename = "monsters.json"
    else:
        filename = "avatars.json"

    if type(creature) not in [Monster, Avatar]:
        raise TypeError("argument must be an instance of the Monster or Avatar class")
    

    with open(filename, "r") as creature_file:
        data = json.load(creature_file)
    
    data[creature.id] = creature.__dict__

    with open(filename, "w") as creature_file:
        data = json.dump(data, creature_file, indent=4)


def delete_creature(creature: str, is_monster: bool):
    if is_monster:
        filename = "monsters.json"
    else:
        filename = "avatars.json"
    
    if type(creature) != str:
        raise TypeError("the id must be a string")
    
    with open(filename, "r") as creature_file:
        data = json.load(creature_file)
    
    del data[creature]

    with open(filename, "w") as creature_file:
        data = json.dump(data, creature_file, indent=4)


def observe_file(file_name: str):
    with open(file_name, "r") as file:
                contents = json.load(file)
                for key in contents:
                    content = Monster(**contents[key])
                    print(content)

def ask_with_type(question: str, result_type: type):
    asking: bool = True 

    while asking:
        answer = input(question).lower().strip()
        
        if result_type == float and (type(character) == int or character in ["."] for character in answer):
            pass # here

def ask_stats(is_monster: bool) -> list:
    if is_monster == True:
        creature = "monster"
    else:
        creature = "avatar"

    creature_id = input(f"what should the id of the {creature} be? \n> ")

    if type(creature_id) != str:
        print("the id must be a string")
    
    else:
        creature_str = input(f"what should the strength of the {creature} be? \n> ")
        creature_dex = input(f"what should the dextarity of the {creature} be? \n> ")
        creature_con = input(f"what should the constitution of the {creature} be? \n> ")

    return [creature_id, creature_str, creature_dex, creature_con]

def ask_delete(is_monster: bool):
    if is_monster:
        filename = "monsters.json"
    else:
        filename = "avatars.json"

    with open(filename, "r") as file:
                creatures = json.load(file)
                for key in creatures:
                    print(key)
                
                deleted_creature = input("\nwhich one would you like to delete? \n> ").lower().strip()

                if deleted_creature not in creatures:
                    print(f"'{deleted_creature}' does not exist")
                else:
                    delete_creature(deleted_creature, True)
                    print(f"{deleted_creature} has be successfully deleted")


edit_on = True

command_list = ["obm", "oba", "adm", "ada", "dem", "dea", "end"]

main_menu = """
--  main menu   --
_action_            _command_
observe monsters    obm
observe avatars     oba
add monster         adm
add avatar          ada
delete monster      dem
delete avatar       dea
end game            end
--  main menu   --
"""

monster_file = "monsters.json"
avatar_file = "avatars.json"

while edit_on:


    print(main_menu)
    command = input("> ").lower().strip()

    match command:
        case _ if command == command_list[0]:
            observe_file(monster_file)
            
        case _ if command == command_list[1]:
            observe_file(avatar_file)

        case _ if command == command_list[2]:
            stats = ask_stats(True)
            save_creature(Monster(stats[0], stats[1], stats[2], stats[3]), True)

        case _ if command == command_list[3]:
            stats = ask_stats(False)
            save_creature(Avatar(stats[0], stats[1], stats[2], stats[3]), False)

        case _ if command == command_list[4]:
            ask_delete(True)

        case _ if command == command_list[5]:
            ask_delete(False)

        case _ if command == command_list[6]:
            print("hava a worderful day.")
            edit_on = False

        case _:
            print(f"I am sorry, but '{command}' is not a valid command.")