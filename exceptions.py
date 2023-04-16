class IncorrectAmountData(Exception):
    """When the amount of data is more or less than we need to use"""


class IncorrectSex(Exception):
    """When sex doesn't equal M or F"""


class IncorrectBirthday(Exception):
    """When you use incorrect order of data or you use incorrect data"""

# Проверка на валидность элементов в основном меню

def enter_first_menu() -> int:
    while True:
        try:
            answer = int(input('What do you want to do?\n'
                               'Enter 1 if you want to add new data\n'
                               'Enter 2 if you want to read file\n'
                               'Enter 3 if you want to exit\n'))
            if 0 <= answer <= 3:
                return answer
        except:
            print("You entered not a number")
        else:
            print("You entered wrong number")
