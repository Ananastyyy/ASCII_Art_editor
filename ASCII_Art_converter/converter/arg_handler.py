import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Перевод JPG в ASCII_Art')
    parser.add_argument('name', type=str, help='Имя JPG файла')
    parser.add_argument('width', nargs='?', type=int, default=320,
                        help='Ширина ASCII_Art\'а (по умолчанию: 320)')
    parser.add_argument('height', nargs='?', type=int, default=240,
                        help='Высота ASCII_Art\'а (по умолчанию: 240)')
    return parser.parse_args()


