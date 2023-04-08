from ASCII_Art_converter.converter.arg_handler import get_args
from ASCII_Art_converter.converter.logic.ascii_art import AsciiArt
from ASCII_Art_converter.converter.logic.image_processing import Image
from ASCII_Art_converter.converter.textfile_handler import TextfileHandler


def main():
    args = get_args()
    textfile_handler = TextfileHandler(args.name)
    name = textfile_handler.get_filename()
    ascii_art = AsciiArt(args.width, args.height)
    ascii_art.convert_brightness_to_ascii(
        Image(f'{name}.jpg')
        .get_pixels(ascii_art.get_size()))

    textfile_handler.create_textfile(
        "\n".join(ascii_art.get_ascii_art_lines()))

    textfile_handler.open_textfile()


if __name__ == '__main__':
    main()
