import unittest

from dosbox.filesystem.drive import *


class DriveTestCase(unittest.TestCase):
    def setUp(self):
        self.drive = Drive("C")
        self.root_dir = self.drive.root_dir

        self.sub_dir1 = Directory("sub_dir1")
        self.root_dir.add(self.sub_dir1)

        self.sub_sub_dir = Directory("subsubdir")
        self.sub_dir1.add(self.sub_sub_dir)

        self.sub_sub_dir2 = Directory("subsubdir2")
        self.sub_dir1.add(self.sub_sub_dir2)

    def test_drive_content(self):
        self.assertIn(self.sub_dir1, self.root_dir.content)

    def test_prompt(self):
        self.assertEqual(self.drive.prompt(), "C:\>")

    def test_current_dir(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_item_from_root_path_with_relative_path(self):
        self.assertEqual(self.drive.item_from_path(self.sub_dir1.path), self.sub_dir1)

    def test_change_dir_to_sub_sub_dir(self):
        self.drive.change_current_dir(self.sub_dir1)

        # Test absolute path
        self.assertEqual(self.drive.item_from_path(self.sub_sub_dir.path), self.sub_sub_dir)

        # Test relative path
        self.assertEqual(self.drive.item_from_path("subsubdir"), self.sub_sub_dir)

    def test_path_name_with_leading_forward_slash(self):
        path = "\\"
        self.assertEqual(self.drive.item_from_path(path), self.drive.root_dir)

        path = "\\sub_dir1"
        self.drive.change_current_dir(self.sub_dir1)
        self.assertEqual(self.drive.item_from_path(path), self.sub_dir1)

    def test_path_name_with_one_dot(self):
        path = "."
        self.drive.change_current_dir(self.sub_dir1)
        self.assertEqual(self.drive.item_from_path(path), self.sub_dir1)

        path = ".\\"
        self.drive.change_current_dir(self.sub_dir1)
        self.assertEqual(self.drive.item_from_path(path), self.sub_dir1)

        path = ".\\sub_dir1"
        self.assertEqual(self.drive.item_from_path(path), self.sub_dir1)

    def test_path_name_with_double_dot(self):
        path = ".."
        self.drive.change_current_dir(self.sub_dir1)
        self.assertEqual(self.drive.item_from_path(path), self.root_dir)

        path = '..\\'
        self.drive.change_current_dir(self.sub_sub_dir)
        self.assertEqual(self.drive.item_from_path(path), self.sub_dir1)

        path = '..\\subsubdir2'
        self.drive.change_current_dir(self.sub_sub_dir)
        self.assertEqual(self.drive.item_from_path(path), self.sub_sub_dir2)

        # path = '.\\..\\subsubdir2'
        # self.drive.change_current_dir(self.sub_sub_dir)
        # self.assertEqual(self.drive.item_from_path(path), self.sub_sub_dir2)