import requests
import json

url = 'https://api.sportsdata.io/v3/nfl/scores/json/Standings/2025?key=fac9abd4ba7f4433b90536d0612396f4'

r = requests.get(url)

website_output = json.load(r.text)


print(website_output['Team'])



