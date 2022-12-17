import battle.calculators as calculators
import copy as copy
import random as random
from os import system


class Type:
    def __init__(self, type_name: str, weaknesses: list, resistances: list, immunity: str = ""):
        self.type_name = type_name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunity = immunity


class Pokemon:
    def __init__(self, name: str, moves: list, stats: dict, type1: Type, type2: Type = None):
        self.name = name
        self.moves = moves
        self.type1 = type1
        self.type2 = type2
        self.stats = stats

    def __repr__(self):
        info = "\n-- POKEMON INFORMATION --\n"
        if self.type2 is not None:
            info += f"{self.name} -- {self.type1.type_name}/{self.type2.type_name}\n"
        else:
            info += f"{self.name} -- {self.type1.type_name}\n"
        info += f"HP: {self.stats['hp']} | SPD: {self.stats['spd']}\n"
        info += f"ATK: {self.stats['atk']} | SP. ATK: {self.stats['sp_atk']}\n"
        info += f"DEF: {self.stats['def']} | SP. DEF: {self.stats['sp_def']}"
        return info


class Move:
    def __init__(self, name, type, category, pwr, acc, desc):
        self.name = name
        self.type = type
        self.category = category
        self.pwr = pwr
        self.acc = acc
        self.desc = desc

    def __repr__(self):
        info = "\n--MOVE INFORMATION --\n"
        info += f"{self.name} - {self.type.type_name}\n"
        info += f"Category: {self.category}\n"
        info += f"Power: {self.pwr}\n"
        info += f"Accuracy: {self.acc}\n"
        info += "------------------\n"
        info += self.desc
        return info


class StatusMove(Move):
    def __init__(self, name: str, type: Type, stat: str, degree: int, target: str, desc: str):
        self.name = name
        self.type = type
        self.category = "status"
        self.pwr = 0
        self.acc = 100
        self.desc = desc
        self.stat = stat
        self.degree = degree
        self.target = target

# --- TYPE LIST ---


ELECTRIC = Type("Electric", ["Ground"], ["Flying"])
GRASS = Type("Grass", ["Fire", "Poison", "Flying", "Bug"],
             ["Electric", "Water", "Ground", "Grass"])
WATER = Type("Water", ["Electric", "Grass"], ["Fire", "Water"])
FIRE = Type("Fire", ["Water", "Ground", "Rock"], ["Bug", "Grass", "Fire"])
FLYING = Type("Flying", ["Electric", "Rock"], ["Grass", "Bug"], "Ground")
BUG = Type("Bug", ["Flying", "Fire", "Rock", "Poison"], ["Grass", "Ground"])
ROCK = Type("Rock", ["Water", "Grass", "Rock"], ["Fire", "Normal", "Flying"])
GROUND = Type("Ground", ["Water", "Grass"], ["Poison", "Rock"], "Electric")
POISON = Type("Posion", ["Psychic", "Ground"], ["Grass", "Bug", "Poison"])
PSYCHIC = Type("Psychic", ["Bug"], ["Psychic"])
NORMAL = Type("Normal", [], [])


# --- POKEMON LIST ---

PIKACHU = Pokemon("Pikachu",
                  moves=[
                      Move("Thunderbolt", ELECTRIC, "special", 95, 85,
                           "A strong electric blast is loosed at the foe."),
                      Move("Tackle", NORMAL, "physical", 70, 100,
                           "Charges the foe with a full-body tackle."),
                      StatusMove("Tail Whip", NORMAL, "def", 1, "opp",
                                 "The user wags its tail cutely, making the foe lower its Defense stat."),
                      Move("Spark", ELECTRIC, "physical", 75, 100, "The user throws an electrically charged tackle at the foe.")],
                  stats={"hp": 145, "atk": 120, "def": 90, "sp_atk": 140, "sp_def": 120, "spd": 130}, type1=ELECTRIC)
CHARIZARD = Pokemon("Charizard",
                    moves=[
                        Move("Flamethrower", FIRE, "special", 90, 100,
                             "The foe is scorched with an intense blast of fire"),
                        Move("Air Slash", FLYING, "special", 75, 95,
                             "The user attacks with a blade of air that slices even the sky."),
                        Move("Slash", NORMAL, "physical", 70, 100,
                             "The target is attacked with a slash of claws or blades."),
                        StatusMove("Scary Face", NORMAL, "spd", 2, "opp",
                                   "Frightens the foe with a scary face to sharply reduce its Speed.")],
                    stats={"hp": 160, "atk": 125, "def": 115, "sp_atk": 140, "sp_def": 115, "spd": 130}, type1=FIRE, type2=FLYING)
BLASTOISE = Pokemon("Blastoise",
                    moves=[
                        Move("Aqua Tail", WATER, "physical", 90, 90,
                             "The user attacks by swinging its tail as if it were a vicious wave in a raging storm. "),
                        StatusMove("Withdraw", WATER, "def", 1, "self",
                                   "The user withdraws its body into its hard shell, raising its Defense."),
                        Move("Rapid Spin", NORMAL, "physical", 50, 100,
                             "Spins the body at high speed to strike the foe."),
                        Move("Water Pulse", WATER, "special", 70, 100,
                             "The user attacks the foe with a pulsing blast of water.")],
                    stats={"hp": 165, "atk": 115, "def": 125, "sp_atk": 115, "sp_def": 135, "spd": 110}, type1=WATER)
VENASAUR = Pokemon("Venasaur",
                   moves=[
                       Move("Venoshock", POISON, "special", 65, 100,
                            "The user drenches the target in a special poisonous liquid."),
                       Move("Seed Bomb", GRASS, "physical", 80, 80,
                            "The user slams a barrage of hard-shelled seeds down on the foe from above. "),
                       StatusMove("Growth", GRASS, "sp_atk", 1, "self",
                                  "The user's body is forced to grow, raising its Sp. Atk."),
                       Move("Razor Leaf", GRASS, "physical", 70, 100,
                            "A sharp-edged leaf is launched to slash at the foe.")],
                   stats={"hp": 165, "atk": 110, "def": 110, "sp_atk": 130, "sp_def": 130, "spd": 110}, type1=GRASS, type2=POISON)
PIDGEOT = Pokemon("Pidgeot", moves=[], stats={}, type1=NORMAL, type2=FLYING)
ONIX = Pokemon("Onix", moves=[], stats={}, type1=ROCK, type2=GROUND)
BEEDRILL = Pokemon("Beedrill", moves=[], stats={}, type1=BUG, type2=POISON)
ALAKAZAM = Pokemon("Alakazam", moves=[], stats={}, type1=PSYCHIC)
GYARADOS = Pokemon("Gyarados", moves=[], stats={}, type1=WATER, type2=FLYING)
CROBAT = Pokemon("Crobat", moves=[], stats={}, type1=POISON, type2=FLYING)

pokemon = {"Pikachu": PIKACHU,
           "Charizard": CHARIZARD,
           "Blastoise": BLASTOISE,
           "Venasaur": VENASAUR}
"""            "Pidgeot": PIDGEOT,
           "Onix": ONIX,
           "Beedrill": BEEDRILL,
           "Alakazam": ALAKAZAM,
           "Gyarados": GYARADOS,
           "Crobat": CROBAT """


def attack(attacker, defender, move):
    system("clear")
    print(f'{attacker.name} used {move.name}!')
    input("")

    # Make an accuracy roll to see if the move hits
    roll = random.randint(0, 100)

    if roll > move.acc:
        system("clear")
        print(f'{attacker.name} missed!')
        input("")
        return

    calculators.calc_damage(attacker, defender, move)


def random_pokemon():
    rand_index = random.randint(0, len(pokemon) - 1)
    return list(pokemon.values())[rand_index]
