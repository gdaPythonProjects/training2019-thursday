from managers.manu import Menu
from managers.input import Input
from managers.calculator import Calculator

if __name__ == "__main__":
    menu_manager = Menu()
    input_manager = Input()
    calculator_manager = Calculator()
    while True:
        menu_manager.print_menu()
        menu_manager.get_menu_option()
        if menu_manager.menu_option == 0:
            break
        elif menu_manager.menu_option == 1:
            input_manager.get_a_from_user()
        elif menu_manager.menu_option == 2:
            input_manager.get_b_from_user()
        elif menu_manager.menu_option == 3:
            input_manager.get_a_b_from_user()
        elif menu_manager.menu_option == 4:
            calculator_manager.add_values(input_manager.a, input_manager.b)
        elif menu_manager.menu_option == 5:
            calculator_manager.sub_values(input_manager.a, input_manager.b)