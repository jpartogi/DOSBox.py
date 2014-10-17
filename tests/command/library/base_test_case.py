import unittest

from dosbox.command.invoker import *

from dosbox.filesystem.drive import *

from tests.console.mock_outputter import *

class CommandBaseTestCase(unittest.TestCase):
    def setUp(self):

        self.drive = Drive("C")
        self.root_dir = self.drive.root_dir

        self.invoker = Invoker()
        self.outputter = MockOutputter()

        self.number_of_dirs_before_test = self.root_dir.num_of_contained_dirs()
        self.number_of_files_before_test = self.root_dir.num_of_contained_files()

    def execute_command(self, command):
        self.invoker.execute_command(command, self.outputter)