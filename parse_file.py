from exceptions import IncorrectSex, IncorrectBirthday, IncorrectAmountData
from datetime import datetime

# Делаем класс для парсингда введенных данных
class Parse_data():
    def __init__(self, input_string):
        self.input_string = input_string
        # Длина введенных элементов которая должна быть
        self.len_need_data = 6
        # На какие окончания могут быть фамилии в пост советском пространстве
        self.end_surname = ('iy', 'ya', 'ov', 'va', 'o', 'in', 'na', 'ev', 'va', 'an', 'ko', 'yk', 'ec', 'k',)
        # На какие окончания могут быть отчества в пост советском пространстве
        self.end_secondname = ('ich', 'vna',)
        # 2 типа пола которые использовали в данном приложении
        self.define_sex = ('m', 'f',)

    def parse(self):
        user = {}
        after_parse = self.input_string.split(" ")
        # Проверка на длину введенных элементов, если не подходит, вызываем исключение
        if len(after_parse) != self.len_need_data:
            raise IncorrectAmountData("You enter incorrect data, try again\n")

        for i in after_parse:
            # Проверка на окончания фамилии
            if i.endswith(self.end_surname):
                user['surname'] = i
                # Проверка на окончания отчества
            elif i.endswith(self.end_secondname):
                user['secondname'] = i
                # Проверка если только цифры, значит телефон
            elif i.isnumeric():
                user['phonenumber'] = i
                # Проверка если только цифры и точки, значит год рождения
            elif i.isalnum() != True:
                user['birthday'] = i
                check_birthday = user['birthday'].split(".")
                # Проверка валидность ввода даты
                if 31 < int(check_birthday[0]) or int(check_birthday[0]) < 1:
                    raise IncorrectBirthday("You use incorrect order of data(dd.mm.yyyy) or you enter incorrect Day\n")
                elif 12 < int(check_birthday[1]) or int(check_birthday[1]) < 1:
                    raise IncorrectBirthday(
                        "You use incorrect order of data(dd.mm.yyyy) or you enter incorrect Month\n")
                elif 1900 > int(check_birthday[2]) or int(check_birthday[2]) > datetime.now().year:
                    raise IncorrectBirthday(
                        "You use incorrect order of data(dd.mm.yyyy) or you enter incorrect Year(between 1900 and 2024\n")
                # Проверка на валидность ввода пола
            elif len(i) == 1:
                if i.lower() not in self.define_sex:
                    raise IncorrectSex("Your sex doesn't equal m or f\n")
                user['sex'] = i
            else:
                # Т.к. имена могут заканчиваться на любые буквы, мы берем лабораторные условия, когда по взаимному
                # исключению из всех оставшихся элементов остается только имя!!
                # В реальности мы бы отдельно запрашивали данные у пользователя, отдельно имя, фамилия, отчество и т.д.
                user['name'] = i
        print(user)
        return (user['surname'], user['name'], user['secondname'], user['sex'], user['birthday'], user['phonenumber'],)

