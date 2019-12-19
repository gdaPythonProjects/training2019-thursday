from models.weather import Weather


class Interpreter:
    @staticmethod
    def from_query(data):
        return Weather(
            city_name=data["name"],
            temp=data["main"]["temp"],
            temp_max=data["main"]["temp_max"],
            temp_min=data["main"]["temp_min"],
            feel=data["main"]["feels_like"],
            humidity=data["main"]["humidity"])

    @staticmethod
    def from_file(data):
        return Weather(
            city_name=data["city_name"],
            temp=data["temp"],
            temp_max=data["temp_max"],
            temp_min=data["temp_min"],
            feel=data["feel"],
            humidity=data["humidity"])
