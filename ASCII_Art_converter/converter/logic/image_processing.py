import os

from PIL import Image as Handler
from bestconfig import Config
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="errors.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


class Image:

    def __init__(self, name: str) -> None:
        self._config = Config()
        image_dir = self._config.get("images")
        image_files = [f for f in os.listdir(image_dir) if
                       os.path.isfile(os.path.join(image_dir, f))]
        image_extensions = ("jpg", "jpeg", "bmp", "png")
        image_file = next((f for f in image_files if f.split(".")[-1].lower()
                           in image_extensions and f.startswith(name)), None)
        if not image_file:
            logging.error(f"FileNotFoundError: Image {name} not found")
        else:
            image_path = os.path.join(image_dir, image_file)
            try:
                self._image = Handler.open(image_path)
            except IOError:
                logging.error(f"IOError: Can't open {image_file}")
            self._size = self._image.size

    def get_pixels(self, new_size: tuple[int, int]) -> tuple[tuple[int]]:
        self._image = self._image.resize(new_size)
        self._image.convert(mode=self._config.get("mode"))
        return self._image.getdata()

    def get_size(self) -> tuple[int, int]:
        return self._size
