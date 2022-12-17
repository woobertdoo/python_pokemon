import battle.battle as battle
from os import system


def selection_menu():
    system("clear")
    print("Choose your Pokemon")
    print("-----------")
    names = ""
    for name in battle.pokemon.keys():
        names += f"{name} | "
    print(names)
    print("For info on a specific pokemon, type 'info' followed by the pokemon's name")
    user_input = input("")
    if user_input.capitalize() in battle.pokemon.keys():
        pokemon = battle.pokemon[user_input.capitalize()]
        system("clear")
        print(f"You've selected {pokemon.name}!")
        input("")
        return pokemon
    elif user_input.split()[0] == "info":
        info_pokemon = user_input.split(" ")[1].capitalize()
        system("clear")
        print(battle.pokemon[info_pokemon])
        input("")
    else:
        print("That pokemon isn't available.")
        input("")


def battle_menu(pokemon):
    while True:
        system("clear")
        print(f"HP: {pokemon.stats['hp']}")
        print("Choose a move")
        print("-----------")
        print(f"{pokemon.moves[0].name} | {pokemon.moves[2].name}")
        print(f"{pokemon.moves[1].name} | {pokemon.moves[3].name}")
        print("For info on a specific move, type 'info' followed by the move's name")
        user_input = input("")
        user_input = user_input.split()
        move_query = ""
        if user_input[0] == "info":
            for word in user_input[1:]:
                move_query += word.capitalize() + " "
            move_query = ' '.join(move_query.split())
            for move in pokemon.moves:
                if move_query == move.name:
                    system("clear")
                    print(move)
                    input("")
        else:
            move_query = ' '.join(user_input)
            for move in pokemon.moves:
                if move_query == move.name:
                    return move
