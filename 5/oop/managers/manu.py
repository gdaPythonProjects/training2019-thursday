from managers.input import Input, WrongInputValue


class Menu:
    def __init__(self):
        self.menu_option = None

    def print_menu(self):
        print("0. Wyjście")
        print("1. Ustaw pole A")
        print("2. Ustaw pole B")
        print("3. Ustaw pole A i B")
        print("4. Dodaj A i B")
        print("5. Odejmij A i B")
        print("6. Pomnóż A i B")
        print("7. Podziel A i B")
        print("8. Reszta z dzielenia A i B")

    def get_menu_option(self):
        try:
            self.menu_option = Input.get_int_from_user("Wybierz opcję z menu: ")
        except WrongInputValue:
            print("Podaj liczbę całkowitą")
