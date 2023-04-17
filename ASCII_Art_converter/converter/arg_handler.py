import argparse
from bestconfig import Config


def get_args():
    config = Config()
    width = config.get('width')
    height = config.get('height')
    parser = argparse.ArgumentParser(description='Перевод JPG в ASCII_Art')
    parser.add_argument('name', type=str, help='Имя JPG файла')
    parser.add_argument('mode', type=str, nargs='?',
                        choices=['ascii', 'ansi'], default='ansi',
                        help='Режим: ascii или ansi\'а (по умолчанию: ansi)')
    parser.add_argument('width', nargs='?', type=int, default=width,
                        help=f'Ширина ASCII_Art\'а (по умолчанию: {width})')
    parser.add_argument('height', nargs='?', type=int, default=height,
                        help=f'Высота ASCII_Art\'а (по умолчанию: {height})')
    return parser.parse_args()
