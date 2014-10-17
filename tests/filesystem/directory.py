import unittest

from dosbox.filesystem.directory import *

class DirectoryTestCase(unittest.TestCase):
    def setUp(self):
        self.root_dir = Directory("root")
        self.sub_dir1 = Directory("subdir1")

    def test_path(self):
        self.root_dir.add(self.sub_dir1)

        self.assertEqual(self.sub_dir1.parent, self.root_dir)
        self.assertEqual(self.sub_dir1.path, "root\subdir1")

    def test_add_remove(self):
        subdir = Directory("subdir")

        self.root_dir.add(subdir)
        self.assertEqual(subdir.parent, self.root_dir)

        self.root_dir.remove(subdir)
        self.assertEqual(subdir.parent, None)

    def test_number_of_contained_file_system_item(self):
        return NotImplemented