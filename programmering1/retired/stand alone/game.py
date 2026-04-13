# classes: wizard, sorcerer, barbarian, fighter
# spells: fireball, fire bolt, ray of frost, eldritch blast, magic missile, chromantic orb, burning hand
# damage type: fire, frost, lightning, force


class Wizard:
    def __init__(self, name, level, spells=None):
        self.name = name
        self.level = level
        self.spells = spells if spells is not None else []

class Sorcerer:
    def __init__(self, name, level, spells=None):
        self.name = name
        self.level = level
        self.spells = spells if spells is not None else []

class Barbarian:
    def __init__(self, name, level, spells=[]):
        self.name = name
        self.level = level

class Fighter:
    def __init__(self, name, level, spells=[]):
        self.name = name
        self.level = level

def learn_spell(spellcaster, spell):
    if type(spellcaster) in [Wizard, Sorcerer]:
        spellcaster.spells.append(spell)
    else:
        raise Exception("only classes Wizard and Sorcerer can learn spells")

def show_spells(spellcaster):
    if type(spellcaster) in [Wizard, Sorcerer]:
        if spellcaster.spells != []:
            print(f"{spellcaster.name} (level {spellcaster.level}) knows:")
            for spell in spellcaster.spells:
                print(f"    - {spell}")
        else:
            print(f"{spellcaster.name} knows NO spells")
    else:
        raise Exception("only classes Wizard and Sorcerer can learn spells")
    

mage1 = Wizard("crazy", 4)
mage2 = Sorcerer("dumb", 3, ["fireball", "ray of frost"])
mage3 = Wizard("carl", 4)

learn_spell(mage3, "fire bullet")

show_spells(mage1)
show_spells(mage2)
show_spells(mage3)