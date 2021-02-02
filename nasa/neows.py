#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = input("Enter a start_date:\n")
    endDate = input("Optionally, enter an end_date:\n")

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + "start_date=" + startdate + "&end_date=" + endDate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata['element_count'])
    
    asteroid_sizes= {}
    danger_count= 0

    for date in neodata["near_earth_objects"].keys():
        for x in neodata["near_earth_objects"][date]:
            asteroid_sizes[x["name"]]= x["estimated_diameter"]["meters"]["estimated_diameter_max"]
            if x["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    biggest_roid = max(asteroid_sizes)
    print(f"biggest roid (meters): {biggest_roid}")
    print(f"number of dangerous asteroids: {danger_count}")

if __name__ == "__main__":
    main()

