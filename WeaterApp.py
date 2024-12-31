import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=49550ef90a1c4bc79ff32715243112&q={city}%22"

r = requests.get(url)
# print(r.text) # if you print direct this line then the line print all details about our city
wdic = json.loads(r.text)
tem = wdic["current"]["temp_c"]
print(tem) # this is give us only city tempreture
engine.say(f"The weather of {city} is {tem} degrees")
engine.runAndWait()