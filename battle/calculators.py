import random
from os import system


def calc_type_mod(defender, move) -> float:
    # Check the pokemon's type (or both if pokemon is dual type) and check if is weak to or resistant to the move type
    # each weakness doubles the move damage, and each resistance halves it
    type_mod = 1.0
    if move.type.type_name in defender.type1.weaknesses:
        type_mod *= 2.0
    elif move.type.type_name in defender.type1.resistances:
        type_mod *= 0.5
    elif move.type.type_name == defender.type1.immunity:
        print("It had no effect!")
        return 0

    if defender.type2 is None:
        if type_mod > 1.0:
            system("clear")
            print("It's super effective!")
            input("")
        elif 0 < type_mod < 1.0:
            system("clear")
            print("It's not very effective!")
            input("")
        return type_mod

    if move.type.type_name in defender.type2.weaknesses:
        type_mod *= 2.0
    elif move.type.type_name in defender.type2.resistances:
        type_mod *= 0.5
    elif move.type.type_name == defender.type1.immunity:
        print("It had no effect!")
        return 0

    if type_mod > 1.0:
        system("clear")
        print("It's super effective!")
        input("")
    elif 0 < type_mod < 1.0:
        system("clear")
        print("It's not very effective!")
        input("")

    return type_mod


def crit_mod() -> int:
    # All damaging attacks have a 12.5% change to critical hit. If they do, they deal double the damage
    if random.random() <= 0.125:
        system("clear")
        print("A critical hit!")
        input("")
        return 2

    return 1


def stab_mod(attacker, move) -> float:
    """
    Calculate Same Type Attack Bonus
    Same Type Attack Bonus increases move damage by 50% if the attacker shares a type with the move
    """
    if move.type == attacker.type1 or move.type == attacker.type2:
        return 1.5

    return 1.0


def calc_damage(attacker, defender, move):
    if move.category == 'status':  # if it's a status move, change the stats of either the opponent or the attacker
        if move.target == 'opp':
            defender.stats[move.stat] -= move.degree
            system("clear")
            print(f"{defender.name}'s {move.stat} was lowered!")
            input("")
        elif move.target == 'self':
            attacker.stats[move.stat] += move.degree
            system("clear")
            print(f"{attacker.name}'s {move.stat} was raised!")
            input("")
        return 0

    damage = 0

    # Calculate base damage including Crit
    damage = 100 * crit_mod()
    damage /= 5
    damage += 2

    # Multiply by the move's damage and the ratio of the attackers atk/sp_atk to the defenders def/sp_def stat
    damage *= move.pwr

    if move.category == 'special':
        damage *= attacker.stats["sp_atk"] / defender.stats["sp_def"]
    elif move.category == 'phyiscal':
        damage *= attacker.stats["atk"] / defender.stats["def"]

    # Divide the damage thus far by 50 then add 2
    damage /= 50
    damage += 2

    # Finally, multiply by the STAB bonus, type modifier, and a random value from 0.85 to 1
    damage *= stab_mod(attacker, move) * calc_type_mod(defender,
                                                       move) * float(random.randint(85, 100) / 100)

    damage = round(damage)
    if damage == 0:
        return

    system("clear")
    print(f'{defender.name} took {damage} damage')
    input("")
    defender.stats['hp'] -= damage
