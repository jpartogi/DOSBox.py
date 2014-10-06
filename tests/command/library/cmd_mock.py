from dosbox.command.framework.command import *

class CmdMock(Command):
    def __init__(self, command_name, drive):
        super().__init__(command_name, drive)
        self.executed = False

    def execute(self, outputter):
        self.executed = True