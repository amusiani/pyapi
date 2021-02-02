#!/usr/bin/python3

import json

def main():
    with open("challenge.json", "r") as data:
        datastring = data.read()
    datadecode = json.loads(datastring)

    for person in datadecode:
        print(f"Name: {person['name']}")
        print(f"Email: {person['email']}")
        print(f"Phone: {person['phone']}")
        print(f"Address: {person['address']}")

    friendsList = []

    for subdictionary in datadecode["friends"]:
        friendsList.append(subdictionary["name"])

    joined_string = ", ".join(friendsList)
 
    print("Friends: " + joined_string + "\n")

main()


