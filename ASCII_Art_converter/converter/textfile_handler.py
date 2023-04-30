import os
import subprocess
from bestconfig import Config


class TextfileHandler:

    def __init__(self, filename: str) -> None:
        config = Config()
        self.__converted_path = config.get("converted")
        self.__filename = filename
        self.__textfile_path = os.path.abspath(
            f'{self.__converted_path}{self.__filename}.txt')

    def create_textfile(self, text: str) -> None:
        try:
            with open(f'{self.__converted_path}'
                      f'{self.__filename}.txt', 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print('FileNotFoundError: Не удалось создать ASCII_Art файл\n')
        except IOError:
            print('IOError: Ошибка ввода-вывода. '
                  'Не удалось создать файл с Ascii_Art\'ом\n')

    def open_textfile(self) -> None:
        try:
            if os.name == 'nt':
                os.startfile(self.__textfile_path)
            elif os.name == 'posix':
                subprocess.run(
                    ['gnome-terminal', '--', 'less', self.__textfile_path])
            else:
                print('Ошибка: операционная система не поддерживается')
        except FileNotFoundError:
            print('FileNotFoundError: Не удалось открыть файл')
        except IOError:
            print('IOError: Ошибка ввода-вывода. Не удалось открыть файл')

    def get_filename(self) -> str:
        return self.__filename
