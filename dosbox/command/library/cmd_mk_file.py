from dosbox.command.framework.command import *

from dosbox.filesystem.file import *

class CmdMkFile(Command):

    def __init__(self, name, drive):
        super().__init__(name, drive)

    def check_number_of_params(self, num_of_params):
        return True

    def check_param_values(self, outputter):
        return True

    def execute(self, outputter):
        file_name = self.param_at(0)
        file_content = self.param_at(1)
        file = File(file_name, file_content)
        self.drive.current_dir.add(file)