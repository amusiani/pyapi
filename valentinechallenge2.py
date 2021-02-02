#!/usr/bin/python3

import json

def main():
    with open("challenge.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)

    # Name
    print(datadecoded[3]["name"])

    # Eye color
    print(datadecoded[3]["eyeColor"])

    # Favorite fruit
    print(datadecoded[3]["favoriteFruit"],"\n")

    print(f"Ah, {datadecoded[3]['name']}.")
    print(f"Eyes like a lime, citrus {datadecoded[3]['eyeColor']}.")
    print(f"Have a {datadecoded[3]['favoriteFruit']}.")

main()
