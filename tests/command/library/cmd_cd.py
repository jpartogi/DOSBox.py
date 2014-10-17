from dosbox.command.library.cmd_cd import *

from dosbox.filesystem.directory import *
from dosbox.filesystem.file import *

from tests.command.library.base_test_case import *


class CmdCdTestCase(CommandBaseTestCase):
    def setUp(self):
        super().setUp()

        self.sub_dir1 = Directory("subdir1")
        self.root_dir.add(self.sub_dir1)
        self.file1_in_sub_dir1 = File("file1subdir1", "")
        self.sub_dir1.add(self.file1_in_sub_dir1)

        self.file1 = File("file1", "")
        self.root_dir.add(self.file1)

        self.command = CmdCd("cd", self.drive)

        self.invoker.add_command(self.command)

    def test_CmdCd_ChangeToSubdirectory_ChangesDirectory(self):
        self.execute_command("cd " + self.sub_dir1.path)
        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_CmdCd_ChangeToSubDirectoryWithEndingBacklash_ChangesDirectory(self):
        self.execute_command("cd " + self.sub_dir1.path + "\\")
        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_CmdCd_WithBacklash_ChangesToRoot(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd \\")

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.root_dir)

    def test_CmdCd_WithPointPoint_ChangesToParent(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd ..")

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.root_dir)

    def test_CmdCd_WithPointPointInRootDir_RemainsInRootDir(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("cd ..")

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.root_dir)

    def test_CmdCd_WithPoint_RemainsInCurrentDirectory(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd .")

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_CmdCd_WithPointInRootDir_RemainsInCurrentDirectory(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("cd .")

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.root_dir)

    def test_CmdCd_WithoutParameter_PrintsCurrentDirectory(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd")

        self.assertIn(self.sub_dir1.path, self.outputter.output)

    def test_CmdCd_WithInvalidAbsolutePath_RemainsInCurrentDirectory(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd c:\\gaga\\gugus")

        self.assertEqual(CmdCd.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED, self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def CmdCd_WithFileAsPath_RemainsInCurrentDirectory(self):
        self.drive.change_current_dir(self.sub_dir1)
        self.execute_command("cd " + self.file1_in_sub_dir1.path)

        self.assertEqual(CmdCd.DESTINATION_IS_FILE, self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_CmdCd_WithRelativePath_ChangesDirectory(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("cd " + self.sub_dir1.name)

        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

    def test_CmdCd_ChangeToNonExistingDirectory_PrintsError(self):
        self.drive.change_current_dir(self.root_dir)
        self.execute_command("cd NonExistingDirectory")

        self.assertEqual(CmdCd.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED, self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.root_dir)

    def test_CmdCd_AllParametersAreReset(self):
        self.drive.change_current_dir(self.root_dir)

        self.execute_command("cd " + self.sub_dir1.path)
        self.assertEqual("", self.outputter.output)
        self.assertEqual(self.drive.current_dir, self.sub_dir1)

        self.execute_command("cd")
        self.assertIn(self.sub_dir1.path, self.outputter.output)
