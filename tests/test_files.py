import unittest
from files import ImageFile
from files import DATA_DIRECTORY
import os
from shutil import copyfile

TEST_FILE = 'digits1'
UNICODE_TEST_FILE = 'unicode1'


class TestImageFile(unittest.TestCase):
    def test_ground(self):
        imgf = ImageFile(TEST_FILE)
        self.assertEqual(imgf.is_grounded, True)
        imgf.set_ground(imgf.ground.segments, imgf.ground.classes, write_file=False)
        self.assertEqual(imgf.is_grounded, True)
        imgf.remove_ground(remove_file=False)
        self.assertEqual(imgf.is_grounded, False)

    def test_ground_unicode(self):
        imgf = ImageFile(UNICODE_TEST_FILE)
        self.assertEqual(imgf.is_grounded, True)
        imgf.set_ground(imgf.ground.segments, imgf.ground.classes, write_file=False)
        self.assertEqual(imgf.is_grounded, True)
        imgf.remove_ground(remove_file=False)
        self.assertEqual(imgf.is_grounded, False)

    def test_open_custom(self):
        # First copy the file to a reachable folder
        digits_path = os.path.join(DATA_DIRECTORY, "digits1.png")
        destination = os.path.join(os.getcwd(), "digits_custom.png")
        copyfile(digits_path, destination)
        file = ImageFile("digits_custom")
        self.assertIsInstance(file, ImageFile)
        os.remove(destination)
