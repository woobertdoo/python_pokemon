from battle import battle, menu
import random
from os import system

my_pokemon = None
opp_pokemon = battle.random_pokemon()

while my_pokemon is None:
    my_pokemon = menu.selection_menu()

while opp_pokemon.name == my_pokemon.name:
    opp_pokemon = battle.random_pokemon()
system("clear")
print(f'The opponent chose {opp_pokemon.name}!')
input("")
while my_pokemon.stats['hp'] > 0 and opp_pokemon.stats['hp'] > 0:
    move = menu.battle_menu(my_pokemon)
    random_index = random.randint(0, 3)
    random_move = opp_pokemon.moves[random_index]

    if my_pokemon.stats['spd'] > opp_pokemon.stats['spd']:
        battle.attack(my_pokemon, opp_pokemon, move)
        if opp_pokemon.stats['hp'] <= 0:
            break
        battle.attack(opp_pokemon, my_pokemon, random_move)
    else:
        battle.attack(opp_pokemon, my_pokemon, random_move)
        if my_pokemon.stats['hp'] <= 0:
            break

        battle.attack(my_pokemon, opp_pokemon, move)


if my_pokemon.stats['hp'] <= 0:
    print("You lost...")
else:
    print('You won!')
