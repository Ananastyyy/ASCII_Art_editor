import unittest

from ASCII_Art_converter.converter.logic.ascii_art import AsciiArt


class AsciiArtTests(unittest.TestCase):

    def test_normalize_brightness(self):
        instance = AsciiArt(320, 240)
        pixels = [(255, 255, 255), (0, 0, 0), (127, 127, 127)]
        expected_result = [1.0, 0.0, 0.45454545454545453]
        self.assertEqual(instance.normalize_brightness(pixels),
                         expected_result)

    def test_normalize_brightness_with_single_pixel(self):
        instance = AsciiArt(320, 240)
        pixels = [(100, 100, 100)]
        expected_result = [1.0]
        self.assertEqual(instance.normalize_brightness(pixels),
                         expected_result)

    def test_convert_brightness_to_ascii(self):
        instance = AsciiArt(320, 240)
        pixels = [(255, 255, 255), (0, 0, 0), (127, 127, 127)]
        expected_result = ' @D'
        instance.convert_brightness_to_ascii(pixels)
        self.assertEqual('\n'.join(instance.get_ascii_art_lines()),
                         expected_result)

    def test_convert_brightness_to_ascii_with_single_pixel(self):
        instance = AsciiArt(320, 240)
        pixels = [(100, 100, 100)]
        expected_result = ' '
        instance.convert_brightness_to_ascii(pixels)
        self.assertEqual('\n'.join(instance.get_ascii_art_lines()),
                         expected_result)

    def test_get_size(self):
        instance = AsciiArt(320, 240)
        expected_result = (320, 240)
        self.assertEqual(instance.get_size(), expected_result)

    def test_get_ascii_art_lines(self):
        instance = AsciiArt(1, 240)
        instance.convert_brightness_to_ascii(
            [(255, 255, 255), (0, 0, 0), (127, 127, 127)])
        expected_result = [' ', '@', 'D']
        self.assertEqual(instance.get_ascii_art_lines(),
                         expected_result)


if __name__ == '__main__':
    unittest.main()
