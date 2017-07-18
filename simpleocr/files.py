import os
from pkg_resources import resource_filename
import cv2
from .tesseract_utils import read_boxfile, write_boxfile

IMAGE_EXTENSIONS = ['.png', '.tif', '.jpg', '.jpeg']
DATA_DIRECTORY = resource_filename("simpleocr", "data")
GROUND_EXTENSIONS = ['.box']
GROUND_EXTENSIONS_DEFAULT = GROUND_EXTENSIONS[0]


def try_extensions(extensions, path):
    """ Checks for various extensions if a path exist if the extension is appended """
    for ext in [""] + extensions:
        if os.path.exists(path + ext):
            return path + ext
    return None


def open_image(path):
    return ImageFile(get_file_path(path))


def get_file_path(path, ground=False):
    """
    Get the absolute path for an image or ground file. Valid inputs are:
    - Relative path with or without extension
    - File in DATA_DIRECTORY with or without extension
    - Absolute path with or without extension
    :param path: image path in str type
    :param ground: whether the file must be a ground file
    :return: The absolute path to the file requested
    """
    extensions = GROUND_EXTENSIONS if ground else IMAGE_EXTENSIONS
    # If the path exists, return the path, but make sure it's an absolute path first
    if os.path.exists(path):
        return os.path.abspath(path)
    # Try to find the file with the passed path with the various extensions
    image_with_extension = try_extensions(extensions, os.path.splitext(path)[0])
    if image_with_extension:
        return os.path.abspath(image_with_extension)
    # The file must be in the data directory if it has not yet been found
    image_datadir = try_extensions(extensions, os.path.join(DATA_DIRECTORY, path))
    if image_datadir:
        return os.path.abspath(image_datadir)
    # The file cannot be found, so raise a FileNotFound Error
    raise IOError


class Ground(object):
    """
    Data class that includes labeled characters of an Image and their positions
    """
    def __init__(self, segments=None, classes=None):
        self.segments = segments
        self.classes = classes

    def write(self):
        pass

    def read(self):
        pass


class GroundFile(Ground):
    """
    Child class of GroundBuffer with file support. This class can write the data
    to a box file so it can be restored when the image file the ground data belongs
    to is opened again.
    """
    def __init__(self, path, segments=None, classes=None):
        """
        :param path: path to the box file
        :param segments: segments to store
        :param classes: classes to store
        """
        Ground.__init__(self, segments=segments, classes=classes)
        self.path = path

    def read(self):
        """ Update the ground data stored by reading the box file from disk """
        self.classes, self.segments = read_boxfile(self.path)

    def write(self):
        """ Write a new box file to disk containing the stored ground data """
        write_boxfile(self.path, self.classes, self.segments)


class Image(object):
    """
    Class to work with an image in memory
    """
    def __init__(self, array, debug=False):
        """
        :param array: array with image data, must be OpenCV compatible
        :param debug: if True, debug prints are enabled
        """
        self._image = array
        self._ground = None
        self._debug = debug

    def set_ground(self, segments, classes):
        """ Creates the ground data in memory """
        if self.is_grounded and self._debug:
            print("Warning: grounding already grounded Image")
        self._ground = Ground(segments=segments, classes=classes)

    def remove_ground(self):
        """ Removes the grounding data in memory for the Image """
        if not self.is_grounded:
            print("Warning: removing ground for Image without ground data")
        self._ground = None

    # These properties prevent the user from altering the attributes stored within
    # the object and thus emphasize the immutability of the object
    @property
    def image(self):
        return self._image

    @property
    def is_grounded(self):
        return not (self._ground is None)

    @property
    def ground(self):
        return self._ground


class ImageFile(Image):
    """
    Complete class that contains functions for creation from file,
    as well as from PIL Images. Also supports grounding in memory.
    """
    def __init__(self, path, debug=False):
        """
        :param path: path to the image to read, must be valid and absolute
        :param debug: if True, debug prints are enabled
        """
        array = cv2.imread(path)
        Image.__init__(self, array, debug=debug)
        self._path = path
        basepath = os.path.splitext(path)[0]
        self._ground_path = try_extensions(GROUND_EXTENSIONS, basepath)
        if self._ground_path:
            self._ground = GroundFile(self._ground_path)
            self._ground.read()
        else:
            self._ground_path = basepath + GROUND_EXTENSIONS_DEFAULT
            self._ground = None

    def set_ground(self, segments, classes, write_file=False):
        """ creates the ground, saves it to a file """
        if self.is_grounded and self._debug:
            print("Warning: grounding already grounded file")
        self._ground = GroundFile(self._ground_path)
        self.ground.segments = segments
        self.ground.classes = classes
        if write_file:
            self.ground.write()

    def remove_ground(self, remove_file=False):
        """ Removes ground, optionally deleting it's file """
        if not self.is_grounded and self._debug:
            print("Warning: ungrounding ungrounded file")
        self._ground = None
        if remove_file:
            os.remove(self._ground_path)

    @property
    def path(self):
        return self._path

    @property
    def ground_path(self):
        return self._ground_path


