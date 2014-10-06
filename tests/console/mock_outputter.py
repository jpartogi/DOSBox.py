import unittest

from dosbox.console.console_outputter import *


class MockOutputter(ConsoleOutputter):
    def __init__(self):
        self.output = ""

    def println(self, text):
        self.output += text
        self.analyse_printed_chars(text)

    def print(self, text):
        self.output += text
        self.analyse_printed_chars(text)

    def newline(self):
        pass

class OutputterTestCase(unittest.TestCase):
    def setUp(self):
        self.outputter = MockOutputter()

    def test_has_chars_printed(self):
        self.outputter.print("dir")

        self.assertEqual(True, self.outputter.has_characters_printed())
        self.assertEqual(3, self.outputter.number_of_printed_chars)
        self.assertEqual("dir", self.outputter.output)