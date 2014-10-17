from dosbox.command.library.cmd_mk_file import *

from tests.command.library.base_test_case import *


class CmdMkFileTestCase(CommandBaseTestCase):
    def setUp(self):
        super().setUp()

        self.command = CmdMkFile("mkfile", self.drive)

        self.invoker.add_command(self.command)

    def test_CmdMkFile_WithContent_CreatesFileWithContent(self):
        file_name = "testFile"
        file_content = "blah"

        self.execute_command("mkfile " + file_name + " " + file_content)
        self.assertEqual(self.number_of_files_before_test + 1, self.root_dir.num_of_contained_files())

        file = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + file_name)
        self.assertEqual(file_content, file.content)