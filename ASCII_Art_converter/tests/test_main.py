import unittest
from unittest.mock import patch

from main import open_textfile


class TestMyModule(unittest.TestCase):
    def test_open_textfile_in_Windows(self):
        with patch('os.name', 'nt'):
            with patch('os.startfile') as m:
                open_textfile('file_path')
                m.assert_called_once_with('file_path')
