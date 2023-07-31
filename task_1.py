# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.


def split_file_path(file_link: str) -> tuple:
    *file_path, file_data = file_link.split('\\')
    file_name, file_extension = file_data.split('.')

    return file_path, file_name, file_extension


my_file_path = 'C:\omele4ka\PycharmProjects\deep_python_hw_4.txt'

print(split_file_path(my_file_path))