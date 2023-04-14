import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Перевод JPG в ASCII_Art')
    parser.add_argument('name', type=str, help='Имя JPG файла')
    parser.add_argument('width', nargs='?', type=int, default=600,
                        help='Ширина ASCII_Art\'а (по умолчанию: 600)')
    parser.add_argument('height', nargs='?', type=int, default=300,
                        help='Высота ASCII_Art\'а (по умолчанию: 300)')
    parser.add_argument('mode', type=str, nargs='?',
                        choices=['ascii', 'ansi'], default='ansi',
                        help='Режим: ascii или ansi\'а (по умолчанию: ansi)')
    return parser.parse_args()


