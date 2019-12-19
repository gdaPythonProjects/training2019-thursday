class Weather:
    def __init__(self, city_name, temp, feel, temp_max, temp_min, humidity):
        self.city_name = city_name
        self.temp = temp
        self.feel = feel
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.humidity = humidity

    def __repr__(self):
        return f"Aktualna warunki pogodowe dla miasta {self.city_name}: \n" \
               f" Temperatura: {self.temp}\n Temperatura odczuwalna: {self.feel}" \
               f"\n Wilgotność: {self.humidity}"
