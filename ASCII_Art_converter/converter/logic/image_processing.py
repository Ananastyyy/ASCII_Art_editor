from PIL import Image as Handler
from bestconfig import Config


class Image:

    def __init__(self, name: str):
        config = Config()
        self.__image = Handler.open(f'{config.get("images")}{name}')
        self.__size = self.__image.size

    def get_pixels(self, new_size: tuple[int, int]):
        self.__image = self.__image.resize(new_size)
        self.__image.convert(mode='RGBA')
        return self.__image.getdata()

    def get_size(self) -> tuple[int, int]:
        return self.__size
