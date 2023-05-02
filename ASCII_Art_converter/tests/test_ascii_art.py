import pytest
from colorama import Fore

from ASCII_Art_converter.converter.logic.ascii_art import AsciiArt
from ASCII_Art_converter.converter.logic.mode import Mode

instance = AsciiArt(320, 240)

normalize_testdata = [
    ([(255, 255, 255), (0, 0, 0), (127, 127, 127)], [1.0, 0.0, 0.45454545454545453]),
    ([(100, 100, 100)], [1.0])
]

convert_to_symbol_testdata = [
    ([(255, 255, 255), (0, 0, 0), (127, 127, 127)], Mode.ASCII, " @D"),
    ([(100, 100, 100)], Mode.ASCII, " "),
    ([(255, 255, 255), (0, 0, 0), (127, 127, 127)], Mode.ANSI, "\x1b[37m \x1b[30m@\x1b[30mD"),
    ([(100, 100, 100)], Mode.ANSI, "\x1b[30m ")
]

rgb_to_ansi_testdata = [
    (255, 255, 255, Fore.WHITE),
    (0, 0, 0, Fore.BLACK),
    (255, 0, 0, Fore.RED),
    (0, 255, 0, Fore.GREEN),
    (0, 0, 255, Fore.BLUE),
    (255, 255, 0, Fore.YELLOW),
    (0, 255, 255, Fore.CYAN),
]


@pytest.mark.parametrize("pixels, expected", normalize_testdata)
def test_normalize_brightness(pixels, expected):
    assert instance.normalize_brightness(pixels) == expected


@pytest.mark.parametrize("pixels, mode, expected", convert_to_symbol_testdata)
def test_convert_brightness_to_symbol(pixels, mode, expected):
    instance.convert_brightness_to_symbol(pixels, mode)
    assert instance.get_ascii_art() == expected


@pytest.mark.parametrize("r, g, b, expected", rgb_to_ansi_testdata)
def test_rgb_to_ansi(r, g, b, expected):
    assert instance.rgb_to_ansi(r, g, b) == expected
