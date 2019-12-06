class WrongInputValue(Exception):
    pass


class Input:
    def __init__(self):
        self.a = None
        self.b = 0

    @staticmethod
    def get_int_from_user(message: str) -> int:
        x = input(message)
        if x.isdigit():
            return int(x)
        else:
            raise WrongInputValue("Podaj liczbę całkowitą :)")

    def get_a_from_user(self):
        self.a = self.get_int_from_user("Podaj liczbę A: ")

    def get_b_from_user(self):
        self.b = self.get_int_from_user("Podaj liczbę B: ")

    def get_a_b_from_user(self):
        self.get_a_from_user()
        self.get_b_from_user()
