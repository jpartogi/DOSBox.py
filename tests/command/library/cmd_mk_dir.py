from dosbox.command.library.cmd_mk_dir import *

from tests.command.library.base_test_case import *

class CmdMkDirTestCase(CommandBaseTestCase):
    def setUp(self):
        super().setUp()

        self.command = CmdMkDir("mkdir", self.drive)

        self.invoker.add_command(self.command)

    def test_CmdMkDir_CreateNewDirectory_NewDirectoryIsAdded(self):
        dir_name = "test1"
        self.execute_command("mkdir " + dir_name)

        directory = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + dir_name)

        self.assertEqual(self.root_dir, directory.parent)
        self.assertEqual(self.number_of_dirs_before_test + 1, self.root_dir.num_of_contained_dirs())

    def test_CmdMkDir_SingleLetterDirectory_NewDirectoryIsAdded(self):
        dir_name = "a"
        self.execute_command("mkdir " + dir_name)

        directory = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + dir_name)

        self.assertEqual(self.root_dir, directory.parent)
        self.assertEqual(self.number_of_dirs_before_test + 1, self.root_dir.num_of_contained_dirs())

    def test_CmdMkDir_NoParameters_ErrorMessagePrinted(self):
        self.execute_command("mkdir")

        self.assertIn(BaseCommand.INCORRECT_SYNTAX, self.outputter.output)

    def test_CmdMkDir_ParameterContainsBacklash_ErrorMessagePrinted(self):
        self.execute_command("mkdir c:\\test1")

        self.assertIn(CmdMkDir.PARAMETER_CONTAINS_BACKLASH, self.outputter.output)
        self.assertRaises(Exception)

    def test_CmdMkDir_ParameterContainsBacklash_NoDirectoryCreated(self):
        self.execute_command("mkdir c:\\test1")

        self.assertEqual(self.number_of_dirs_before_test, self.root_dir.num_of_contained_dirs())

    def test_CmdMkDir_SeveralParameters_SeveralNewDirectoriesCreated(self):
        test_dir_name_1 = "test1"
        test_dir_name_2 = "test2"
        test_dir_name_3 = "test3"

        self.execute_command("mkdir " + test_dir_name_1 + " " + test_dir_name_2 + " " + test_dir_name_3)
        self.assertEqual(self.number_of_dirs_before_test + 3, self.root_dir.num_of_contained_dirs())

        directory_1 = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + test_dir_name_1)
        directory_2 = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + test_dir_name_2)
        directory_3 = self.drive.item_from_path(self.drive.drive_letter_colon + "\\" + test_dir_name_3)

        self.assertEqual(self.root_dir, directory_1.parent)
        self.assertEqual(self.root_dir, directory_2.parent)
        self.assertEqual(self.root_dir, directory_3.parent)

    def test_CmdMkDir_AllParametersAreReset(self):
        dir_name = "test1"
        self.execute_command("mkdir " + dir_name)
        self.assertEqual(self.number_of_dirs_before_test + 1, self.root_dir.num_of_contained_dirs())

        self.execute_command("mkdir")

        self.assertEqual(self.number_of_dirs_before_test + 1, self.root_dir.num_of_contained_dirs())
        self.assertEqual(BaseCommand.INCORRECT_SYNTAX, self.outputter.output)
