import unittest

from dosbox.filesystem.file_system_item import *

class FileSystemItemTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_name(self):
        with self.assertRaises(Exception):
            FileSystemItem("bar\\foo", None)
            FileSystemItem("name,name", None)
            FileSystemItem("bar/foo,baz ", None)

        name = "name"
        item = FileSystemItem(name, None)

        self.assertEqual(name, item.name)
        self.assertEqual(name, str(item))