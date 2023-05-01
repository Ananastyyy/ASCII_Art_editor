from bestconfig import Config
from colorama import Fore


class AsciiArt:
    _config = Config()
    _ascii_chars = _config.get("ascii_chars")
    _colors = {0: {0: {0: Fore.BLACK, 1: Fore.BLUE},
                   1: {0: Fore.GREEN, 1: Fore.CYAN}},
               1: {0: {0: Fore.RED, 1: Fore.MAGENTA},
                  1: {0: Fore.YELLOW, 1: Fore.WHITE}}}

    def __init__(self, width: int, height: int) -> None:
        self._ascii_art = ""
        self._threshold = self._config.get("threshold")
        self.__width = width
        self.__height = height

    def rgb_to_ansi(self, r, g, b) -> Fore:
        return self._colors[round(r / 255)][round(g / 255)][round(b / 255)]

    def normalize_brightness(self, pixels: any) -> list[int]:
        brightness_values = [sum(pixel) //
                             self._threshold for pixel in pixels]

        max_brightness = max(brightness_values)
        return [value / max_brightness for value in brightness_values]

    def ascii_symbol(self, _, value: int) -> str:
        return self._ascii_chars[int(value * (len(self._ascii_chars) - 1))]

    def ansi_symbol(self, pixels: tuple, value: int) -> str:
        return self.rgb_to_ansi(*pixels) + self._ascii_chars[
            int(value * (len(self._ascii_chars) - 1))]

    def convert_brightness_to_symbol(self, pixels: any, mode: str) -> None:
        self._ascii_art = ""
        normalized_brightness = self.normalize_brightness(pixels)
        operation = self.ansi_symbol if mode == "ansi" else self.ascii_symbol
        for i, value in enumerate(normalized_brightness):
            char = operation(pixels[i], value)
            if (i + 1) % self.__width == 0:
                char += "\n"
            self._ascii_art += char

    def get_size(self) -> tuple[int, int]:
        return self.__width, self.__height

    def get_ascii_art(self) -> str:
        if self._ascii_art:
            return self._ascii_art
