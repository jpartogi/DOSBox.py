from dosbox.command.framework.command import *

from dosbox.filesystem.directory import *


class CmdMkDir(Command):
    PARAMETER_CONTAINS_BACKLASH = "At least one parameter denotes a path rather than a directory name."

    def __init__(self, name, drive):
        super().__init__(name, drive)

    def check_number_of_params(self, num_of_params):
        return True if num_of_params >= 1 else False

    def check_param_values(self, outputter):
        for i in range(self.params_count()):
            if self.parameter_contains_backlashes(self.params[i], outputter):
                return False

        return True

    def execute(self, outputter):
        for i in range(self.params_count()):
            self.create_directory(self.params[i], self.drive)

    def parameter_contains_backlashes(self, param, outputter):
        if "\\" in param or "/" in param:
            outputter.println(self.PARAMETER_CONTAINS_BACKLASH)
            return True

        return False

    def create_directory(self, dir_name, drive):
        directory = Directory(dir_name)
        drive.current_dir.add(directory)