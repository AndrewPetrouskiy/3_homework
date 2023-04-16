from parse_file import Parse_data
from files import *
from exceptions import *

# Вьюшка для пользователя которая работает с клиентом

class View():
    @staticmethod
    def run():
        print("Hello, welcome to my app.")
        while True:
            try:
                num = enter_first_menu()
                if num == 1:
                    parse_str = input('Enter name, surname, second name, date of birth(format: dd.mm.yyyy),'
                                      ' sex(format: f or m), phone number(format: 375295737234). The format of data must be '
                                      'separated by space\n')
                    for_parse = Parse_data(parse_str)
                    try:
                        user = for_parse.parse()
                    except IncorrectBirthday as ex:
                        print(ex)
                    except IncorrectSex as ex:
                        print(ex)
                    except IncorrectAmountData as ex:
                        print(ex)
                    else:
                        FileOperation.save_lines(name=user[0], line=user)
                if num == 2:
                    name_of_file = input('Enter the name of file which you want to read')
                    FileOperation.read_lines(name_of_file)
                if num == 3:
                    print("Thank you that you use my app")
                    break
            except KeyboardInterrupt:
                print('You enterrupted this action')
