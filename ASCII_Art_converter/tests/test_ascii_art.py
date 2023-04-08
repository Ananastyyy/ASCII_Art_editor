import unittest

from ASCII_Art_converter.converter.logic.ascii_art import AsciiArt


class AsciiArtTests(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = AsciiArt(320, 240)

    def test_normalize_brightness(self):
        pixels = [(255, 255, 255), (0, 0, 0), (127, 127, 127)]
        expected_result = [1.0, 0.0, 0.45454545454545453]
        self.assertEqual(self.instance.normalize_brightness(pixels),
                         expected_result)

    def test_normalize_brightness_with_single_pixel(self):
        pixels = [(100, 100, 100)]
        expected_result = [1.0]
        self.assertEqual(self.instance.normalize_brightness(pixels),
                         expected_result)

    def test_convert_brightness_to_ascii(self):
        pixels = [(255, 255, 255), (0, 0, 0), (127, 127, 127)]
        expected_result = ' @D'
        self.instance.convert_brightness_to_ascii(pixels)
        self.assertEqual('\n'.join(self.instance.get_ascii_art_lines()),
                         expected_result)

    def test_convert_brightness_to_ascii_with_single_pixel(self):
        pixels = [(100, 100, 100)]
        expected_result = ' '
        self.instance.convert_brightness_to_ascii(pixels)
        self.assertEqual('\n'.join(self.instance.get_ascii_art_lines()),
                         expected_result)

    def test_get_size(self):
        expected_result = (320, 240)
        self.assertEqual(self.instance.get_size(), expected_result)

    def test_get_ascii_art_lines(self):
        self.instance.convert_brightness_to_ascii(
            [(255, 255, 255), (0, 0, 0), (127, 127, 127)])
        expected_result = [' ', '@', 'D']
        self.assertEqual(self.instance.get_ascii_art_lines(),
                         expected_result)


if __name__ == '__main__':
    unittest.main()
