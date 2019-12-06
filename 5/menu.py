class Menu:
    def print_menu(self):
        print("0. Exit")
        print("1. GetValue")
        print("2. Wypisz mi coś tam")
        print(self.__x)

    def __init__(self):
        self.__x = 10
        print("Hello! :)")

    def __del__(self):
        print("Papa!")
