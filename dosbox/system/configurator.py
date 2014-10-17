from dosbox.command.factory import *
from dosbox.command.invoker import *
from dosbox.console.console import *
from dosbox.filesystem.drive import *


class Configurator(object):
    def configure_system(self):
        drive = Drive("C")
        drive.restore()

        command_factory = Factory(drive)
        command_invoker = Invoker()
        command_invoker.commands = command_factory.commands

        console = Console(command_invoker, drive)
        console.process_input()