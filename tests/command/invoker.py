import unittest

from dosbox.command.invoker import *

from dosbox.filesystem.drive import *

from tests.command.library.cmd_mock import *

from tests.console.mock_outputter import *

class InvokerTestCase(unittest.TestCase):
    def setUp(self):
        self.invoker = Invoker()
        self.outputter = MockOutputter()
        self.drive = Drive("C")
        self.command = CmdMock("dir", self.drive)
        self.invoker.add_command(self.command)

    def test_parse_command_name_empty_string(self):
        self.assertEqual("", self.invoker.parse_command_name(""))

    def test_parse_command_name_only(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir"))

    def test_parse_command_name_upper_case(self):
        self.assertEqual("dir", self.invoker.parse_command_name("DIR"))

    def test_parse_command_name_with_one_letter_param(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir param1"))

    def test_parse_command_name_one_param(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir param1"))

    def test_parse_command_name_with_comma(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir,"))

    def test_parse_command_name_with_white_spaces(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir   "))

    def test_parse_command_name_with_separator(self):
        self.assertEqual("dir", self.invoker.parse_command_name("dir,param1, param2"))

    def test_parse_one_param(self):
        params = self.invoker.parse_command_params("dir /p")

        self.assertEqual(1, len(params))
        self.assertEqual("/p", params[0])

    def test_parse_two_params(self):
        params = self.invoker.parse_command_params("dir /p param1")

        self.assertEqual(2, len(params))
        self.assertEqual("/p", params[0])
        self.assertEqual("param1", params[1])

    def test_parse_two_params_with_single_chars(self):
        params = self.invoker.parse_command_params("dir a b")

        self.assertEqual("a", params[0])
        self.assertEqual("b", params[1])

    def test_parse_two_params_with_spaces(self):
        params = self.invoker.parse_command_params("dir    param1     param2")

        self.assertEqual("param1", params[0])
        self.assertEqual("param2", params[1])

    def test_parse_three_params(self):
        params = self.invoker.parse_command_params("dir a b c")

        self.assertEqual(3, len(params))

    def test_simple_command(self):
        self.invoker.execute_command("dir", self.outputter)
        self.assertTrue(self.command.executed)

    def test_command_with_params(self):
        self.invoker.execute_command("dir a b", self.outputter)
        self.assertTrue(self.command.executed)
        self.assertEqual(2, self.command.num_of_params())