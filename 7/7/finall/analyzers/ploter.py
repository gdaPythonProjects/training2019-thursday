from matplotlib import pyplot as plt

class Ploter:
    def __init__(self, weathers):
        self.weathers = weathers

    def temperature_plot(self):
        x = [o.city_name for o in self.weathers]
        y = [o.feel for o in self.weathers]
        print(x)
        print(y)
        plt.plot(x, y)
        plt.savefig("xd.png")
