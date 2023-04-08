import argparse
import os
import subprocess

from ASCII_Art_converter.converter.logic.ascii_art import AsciiArt
from ASCII_Art_converter.converter.logic.image_processing import Image


def get_args():
    parser = argparse.ArgumentParser(description='Перевод JPG в ASCII_Art')
    parser.add_argument('name', type=str, help='Имя JPG файла')
    parser.add_argument('width', nargs='?', type=int, default=320,
                        help='Ширина ASCII_Art\'а (по умолчанию: 320)')
    parser.add_argument('height', nargs='?', type=int, default=240,
                        help='Высота ASCII_Art\'а (по умолчанию: 240)')
    return parser.parse_args()


def create_textfile(filename: str, text: str):
    try:
        with open(f"ASCII_Art_converter/images_converted/{filename}.txt", "w") as file:
            file.write(text)
    except FileNotFoundError:
        print("FileNotFoundError: Не удалось создать файл с ASCII_Art'ом\n")
    except IOError:
        print("IOError: Ошибка ввода-вывода. "
              "Не удалось создать файл с Ascii_Art'ом\n")


def open_textfile(filepath):
    try:
        if os.name == 'nt':
            os.startfile(filepath)
        elif os.name == 'posix':
            subprocess.run(['gnome-terminal', '--', 'less', filepath])
        else:
            print('Ошибка: операционная система не поддерживается')
    except FileNotFoundError:
        print("FileNotFoundError: Не удалось открыть файл")
    except IOError:
        print("IOError: Ошибка ввода-вывода. Не удалось открыть файл")


def main():
    args = get_args()

    name = args.name
    ascii_art = AsciiArt(args.width, args.height)
    ascii_art.convert_brightness_to_ascii(Image(f"ASCII_Art_converter/images/{name}.jpg").
                                          get_pixels(ascii_art.get_size()))

    create_textfile(name, "\n".join(ascii_art.get_ascii_art_lines()))
    path = os.path.abspath(f"ASCII_Art_converter/images_converted/{name}.txt")

    open_textfile(path)


if __name__ == "__main__":
    main()
