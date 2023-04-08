from bestconfig import Config


class AsciiArt:
    config = Config()
    ascii_chars = config.get("ascii_chars")

    def __init__(self, width: int, height: int):
        self.__ascii_art = None
        self.__threshold = 64
        self.__width = width
        self.__height = height

    def normalize_brightness(self, pixels: any) -> list[int]:
        brightness_values = [sum(pixel) //
                             self.__threshold for pixel in pixels]

        max_brightness = max(brightness_values)
        return [value / max_brightness for value in brightness_values]

    def convert_brightness_to_ascii(self, pixels: any):
        normalized_brightness = self.normalize_brightness(pixels)
        ascii_image = ''.join(
            [self.ascii_chars[int(value * (len(self.ascii_chars) - 1))]
             for value in normalized_brightness])
        self.__ascii_art = [ascii_image[i:i + self.__width]
                            for i in range(0, len(ascii_image), self.__width)]

    def get_size(self):
        return self.__width, self.__height

    def get_ascii_art_lines(self) -> list[str]:
        if self.__ascii_art:
            return self.__ascii_art
