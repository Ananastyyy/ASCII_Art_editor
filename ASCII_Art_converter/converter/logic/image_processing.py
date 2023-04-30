from PIL import Image as Handler
from bestconfig import Config


class Image:

    def __init__(self, name: str) -> None:
        self._config = Config()
        self._image = Handler.open(f'{self._config.get("images")}{name}')
        self._size = self._image.size

    def get_pixels(self, new_size: tuple[int, int]) -> tuple[tuple[int]]:
        self._image = self._image.resize(new_size)
        self._image.convert(mode=self._config.get("mode"))
        return self._image.getdata()

    def get_size(self) -> tuple[int, int]:
        return self._size
