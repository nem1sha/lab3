import json


def appgreat(thirst_pokemon, second_pokemon):
    stats_1 = []
    stats_2 = []
    keys = ["hp", "attack", "defense", "sp.atk", "sp.def", "speed", "total"]

    for pokemon in pokemon_full_list:
        if pokemon['name'] == thirst_pokemon:
            for key in keys:
                stats_1.append(pokemon['stats'][key])

    for pokemon in pokemon_full_list:
        if pokemon['name'] == second_pokemon:
            for key in keys:
                stats_2.append(pokemon['stats'][key])

    progresses = [j - k for k, j in zip(stats_1, stats_2)]
    progress = dict(zip(keys, progresses))
    print(progress)


def evolve_pokemon():
    pokemon_name = input('Введите имя покемона:')
    for pokemon in pokemon_full_list:
        if pokemon['name'] == pokemon_name:
            if len(pokemon['evolution']) == 1:
                print('нет эволюций')
            elif len(pokemon['evolution']) == 2:
                if pokemon_name == pokemon['evolution'][0]:
                    print(pokemon['evolution'][1])
                    appgreat(pokemon_name, pokemon['evolution'][1])
                else:
                    print('нет эволюций')
            elif len(pokemon['evolution']) == 3:
                if pokemon_name == pokemon['evolution'][0]:
                    print(pokemon['evolution'][1])
                    appgreat(pokemon_name, pokemon['evolution'][1])
                elif pokemon_name == pokemon['evolution'][1]:
                    print(pokemon['evolution'][2])
                    appgreat(pokemon_name, pokemon['evolution'][2])
                else:
                    print('нет эволюций')


file = open('pokemon_full.json')
pokemon_full = file.read()
pokemon_full_list = json.loads(pokemon_full)
print(evolve_pokemon())