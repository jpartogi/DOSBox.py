from dosbox.command.framework.command import *


class CmdCd(Command):
    SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED = "The system cannot find the path specified."
    DESTINATION_IS_FILE = "The directory name is invalid."

    def __init__(self, name, drive):
        super().__init__(name, drive)
        self.destination_directory = None

    def check_number_of_params(self, num_of_params):
        return num_of_params == 0 or num_of_params == 1

    def check_param_values(self, outputter):
        if self.params_count() > 0:
            self.destination_directory = self.extract_and_check_if_valid_directory(self.param_at(0), self.drive, outputter)
            return self.destination_directory is not None

        return True

    def execute(self, outputter):
        if self.params_count() == 0:
            self.print_current_directory_path(self.drive.current_dir.path(), outputter)
        else:
            self.change_current_directory(self.destination_directory, self.drive, outputter)

    def change_current_directory(self, destination_directory, drive, outputter):
        success = self.drive.change_current_dir(destination_directory)

        if not success:
            outputter.println(self.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED)

    def print_current_directory_path(self, current_directory_name, outputter):
        outputter.println(current_directory_name)

    def extract_and_check_if_valid_directory(self, destination_directory_name, drive, outputter):
        tmp_dir = self.drive.item_from_path(destination_directory_name)

        if tmp_dir is None:
            outputter.println(self.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED)
            return None

        if not tmp_dir.is_directory():
            outputter.println(self.DESTINATION_IS_FILE)
            return None

        return tmp_dir