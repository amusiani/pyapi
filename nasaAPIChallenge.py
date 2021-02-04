#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=gT8fYoCsl1LkiFELTUe1kBKSPpMgxAVoVGwSmG6F").json()
    
    for photo in roverresp["photos"]:
        #print(photo["img_src"])
        print("ROVER: " + photo["rover"]["name"])
        print("DATE: " + photo["earth_date"])
        print(photo["img_src"])
        print("\n")

    #print(len(roverresp["photos"]))

if __name__ == "__main__":
    main()
