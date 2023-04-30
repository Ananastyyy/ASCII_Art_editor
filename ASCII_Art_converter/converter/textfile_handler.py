import os
import subprocess
from bestconfig import Config


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
            print("FileNotFoundError: Не удалось создать ASCII_Art файл\n")
        except IOError:
            print("IOError: Ошибка ввода-вывода. "
                  "Не удалось создать файл с Ascii_Art\"ом\n")

    def open_textfile(self) -> None:
        try:
            if os.name == "nt":
                os.startfile(self._textfile_path)
            elif os.name == "posix":
                subprocess.run(
                    ["gnome-terminal", "--", "less", self._textfile_path])
            else:
                print("Ошибка: операционная система не поддерживается")
        except FileNotFoundError:
            print("FileNotFoundError: Не удалось открыть файл")
        except IOError:
            print("IOError: Ошибка ввода-вывода. Не удалось открыть файл")

    def get_filename(self) -> str:
        return self._filename
