from bestconfig import Config
from colorama import Fore


class AsciiArt:
    config = Config()
    ascii_chars = config.get("ascii_chars")
    colors = {0: {0: {0: Fore.BLACK, 1: Fore.BLUE}, 1: {0: Fore.GREEN, 1: Fore.CYAN}},
              1: {0: {0: Fore.RED, 1: Fore.MAGENTA}, 1: {0: Fore.YELLOW, 1: Fore.WHITE}}}

    def __init__(self, width: int, height: int):
        self.__ascii_art = ""
        self.__threshold = 64
        self.__width = width
        self.__height = height

    def rgb_to_ansi(self, r, g, b):
        return self.colors[round(r / 255)][round(g / 255)][round(b / 255)]

    def normalize_brightness(self, pixels: any) -> list[int]:
        brightness_values = [sum(pixel) //
                             self.__threshold for pixel in pixels]

        max_brightness = max(brightness_values)
        return [value / max_brightness for value in brightness_values]

    def convert_brightness_to_ascii(self, pixels: any):
        normalized_brightness = self.normalize_brightness(pixels)
        for i, value in enumerate(normalized_brightness):
            char = self.rgb_to_ansi(*pixels[i]) + self.ascii_chars[int(value * (len(self.ascii_chars) - 1))]
            if (i + 1) % self.__width == 0:
                char += "\n"
            self.__ascii_art += char

    def get_size(self):
        return self.__width, self.__height

    def get_ascii_art(self) -> str:
        if self.__ascii_art:
            return self.__ascii_art
