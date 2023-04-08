import os
import subprocess


class TextfileHandler:

    def __init__(self, filename: str) -> None:
        self.__filename = filename
        self.__textfile_path = os.path.abspath(
            f'ASCII_Art_converter/images_converted/{self.__filename}.txt')

    def create_textfile(self, text: str) -> None:
        try:
            with open(f'ASCII_Art_converter/images_converted/'
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
