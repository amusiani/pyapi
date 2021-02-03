#!/usr/bin/python3

import requests
import pandas as pd

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()
    # pokemon_df = pd.read_json(pokemon)
    pokemons = []

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        # print(poke.get("name"))
        pokemons.append(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

    pokemonsdf = pd.DataFrame(pokemons)

    pokemonsdf.to_excel("pokemons.xlsx", index = False)
    pokemonsdf.to_csv("pokemons.txt", index=False, header=False, sep=' ')
    pokemonsdf.to_json("pokemons.json")
    

if __name__ == "__main__":
    main()

