import csv
from os import path


class FileOperation():
    # метод для считывание файла
    # контекстный менеджер with() самостоятельно закрывает файл, даже в случае ошибки
    @staticmethod
    def read_lines(file_path):
        try:
            with open(f"{file_path}.csv", encoding='utf-8') as r_file:
                # Создаем объект reader, указываем символ-разделитель " "
                file_reader = csv.reader(r_file, delimiter=" ")
                for row in file_reader:
                    print(row)
        except FileNotFoundError:
            print(f"requested file {file_path}.csv not found")

    @staticmethod
    def save_lines(*, name, line):
        if not path.exists(f"{name}.csv"):
            with open(f"{name}.csv", mode="w", encoding='utf-8') as w_file:
                # создаем объект writer с разделителем " "
                file_writer = csv.writer(w_file, delimiter=" ", lineterminator="\r")
                # создаем первую строку с заголовками
                file_writer.writerow(['Surname', 'Secondname', 'Name', 'Sex', 'Birthday', 'PhoneNumber'])
                # заполняем файл
                file_writer.writerow(line)
        else:
            with open(f"{name}.csv", mode="a", encoding='utf-8') as w_file:
                # создаем объект writer с разделителем " "
                file_writer = csv.writer(w_file, delimiter=" ", lineterminator="\r")
                # заполняем файл
                file_writer.writerow(line)
