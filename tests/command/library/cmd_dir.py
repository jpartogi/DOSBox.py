from dosbox.filesystem.drive import *
from dosbox.filesystem.directory import *
from dosbox.filesystem.file import *

from dosbox.command.library.cmd_dir import *

from tests.command.library.base_test_case import *


class CmdDirTestCase(CommandBaseTestCase):
    def setUp(self):
        super().setUp()

        self.sub_dir1 = Directory("subdir1")
        self.root_dir.add(self.sub_dir1)
        self.file1_in_sub_dir1 = File("file1subdir1", "")
        self.sub_dir1.add(self.file1_in_sub_dir1)

        self.file1 = File("file1", "")
        self.root_dir.add(self.file1)

        self.command = CmdDir("dir", self.drive)

        self.invoker.add_command(self.command)

    def test_cmd_dir_without_parameter_print_path_of_current_directory(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir")
        self.assertIn(self.root_dir.path(), self.outputter.output)

    def test_cmd_dir_without_parameter_print_files(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir")
        self.assertIn(self.file1.name, self.outputter.output)

    def test_cmd_dir_without_parameter_print_dirs(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir")
        self.assertIn(self.sub_dir1.name, self.outputter.output)

    def test_cmd_dir_without_parameter_print_footer(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir")
        self.assertIn("1 File(s)", self.outputter.output)
        self.assertIn("1 Dir(s)", self.outputter.output)

    def test_cmd_dir_path_as_parameter_print_given_path(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir c:\\subdir1")
        self.assertIn(self.file1_in_sub_dir1.name, self.outputter.output)

    def test_CmdDir_PathAsParameter_PrintFilesInGivenPath(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir c:\\subdir1")
        self.assertIn(self.file1_in_sub_dir1.name, self.outputter.output)

    def test_CmdDir_PathAsParameter_PrintsFooter(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir c:\\subdir1")
        self.assertIn("1 File(s)", self.outputter.output)

    def test_CmdDir_FileAsParameter_PrintGivenPath(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir " + self.file1_in_sub_dir1.path())
        self.assertIn(self.sub_dir1.path(), self.outputter.output)

    def test_CmdDir_FileAsParameter_PrintFilesInGivenPath(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir " + self.file1_in_sub_dir1.path())
        self.assertIn("1 File(s)", self.outputter.output)

    def test_CmdDir_FileAsParameter_PrintsFooter(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir " + self.file1_in_sub_dir1.path())
        self.assertIn(self.file1_in_sub_dir1.name, self.outputter.output)

    def test_cmd_dir_non_existing_directory_print_error(self):
        self.execute_command("dir non_existing_dir")
        self.assertIn(CmdDir.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED, self.outputter.output)

    def test_CmdDir_AllParametersAreReset(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("dir c:\\subdir1")
        self.assertIn(self.sub_dir1.name, self.outputter.output)

        self.execute_command("dir")
        self.assertIn(self.root_dir.name, self.outputter.output)