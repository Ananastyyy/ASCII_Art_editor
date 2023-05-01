import os
import subprocess
from bestconfig import Config
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="errors.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


class TextfileHandler:

    def __init__(self, filename: str) -> None:
        config = Config()
        self._converted_path = config.get("converted")
        self._filename = filename
        self._textfile_path = os.path.abspath(
            f"{self._converted_path}{self._filename}.txt")

    def create_textfile(self, text: str) -> None:
        try:
            with open(f"{self._converted_path}"
                      f"{self._filename}.txt", "w") as file:
                file.write(text)
        except FileNotFoundError:
            logging.exception("FileNotFoundError: Не удалось создать Ascii_Art")
        except IOError:
            logging.exception("IOError: Не удалось создать Ascii_Art")

    def open_textfile(self) -> None:
        try:
            if os.name == "nt":
                os.startfile(self._textfile_path)
            elif os.name == "posix":
                subprocess.run(
                    ["gnome-terminal", "--", "less", self._textfile_path])
            else:
                logging.exception("Ошибка: Операционная система не поддерживается")
        except FileNotFoundError:
            logging.exception("FileNotFoundError: Не удалось открыть файл")
        except IOError:
            logging.exception("IOError: Не удалось открыть файл")

    def get_filename(self) -> str:
        return self._filename
