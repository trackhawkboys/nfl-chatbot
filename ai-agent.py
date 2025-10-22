from openai import OpenAI
from helper_function import *


data = nfl_standing_data()
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=f"By looking at {data}, answer the following questions for me....What is the number one team in nfc conference"
)

print(response.output_text)





