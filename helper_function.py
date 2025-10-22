import requests
import json

def nfl_standing_data():
    year=input("Enter the year you'd like to look at:")

    url = f'https://api.sportsdata.io/v3/nfl/scores/json/Standings/{year}?key=fac9abd4ba7f4433b90536d0612396f4'

    response = requests.get(url)
    data = response.json()
    return data




