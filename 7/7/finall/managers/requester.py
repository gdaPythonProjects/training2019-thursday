import requests

from managers.interpreter import Interpreter


class Requester:
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"

    def get_weather(self, city):
        response = requests.get(self.url.format(city=city, token="60484fd1327cc890f7eca48d1143656c"))
        if response.status_code == 200:
            return Interpreter.from_query(response.json())
        else:
            print("Some error during API connection")
