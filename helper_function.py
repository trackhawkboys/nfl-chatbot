import requests
import json

def nfl_standing_data():
    year=input("Enter the year you'd like to look at:")

    url = f'https://api.sportsdata.io/v3/nfl/scores/json/Standings/{year}?key=fac9abd4ba7f4433b90536d0612396f4'

    response = requests.get(url)
    data = response.json()
    data_string = json.dumps(data)
    return data_string


data = nfl_standing_data()
print(data)


# with open("nfl_season_information.txt", "a") as f:
#   f.write(data)

# #open and read the file after the appending:
# with open("nfl_season_information.txt") as f:
#   print(f.read())
