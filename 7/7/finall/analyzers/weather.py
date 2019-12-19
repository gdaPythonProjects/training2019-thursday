class WeatherAnalyzer:
    def __init__(self, weathers):
        weathers.sort(key=lambda x: x.temp)
        self.weathers = weathers

    def coldest(self):
        print("Najzimniejsza temperatura panuje w mieście {}. Temperatura wynosi {}".
              format(self.weathers[0].city_name, self.weathers[0].temp))

    def print_all_weathers(self):
        for i in self.weathers:
            print(i)
