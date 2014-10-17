from dosbox.command.base_command import *


class CmdCd(BaseCommand):
    SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED = "The system cannot find the path specified."
    DESTINATION_IS_FILE = "The directory name is invalid."

    def __init__(self, name, drive):
        super().__init__(name, drive)
        self.destination_directory = None

    def check_number_of_params(self, num_of_params):
        return num_of_params == 0 or num_of_params == 1

    def check_param_values(self, outputter):
        if self.num_of_params() > 0:
            self.destination_directory = self.extract_and_check_if_valid_directory(self.param(0), outputter)
            return self.destination_directory is not None

        return True

    def execute(self, outputter):
        if self.num_of_params() == 0:
            self.print_current_directory_path(self.drive.current_dir.path, outputter)
        else:
            self.change_current_directory(self.destination_directory, outputter)

    def change_current_directory(self, destination_directory, outputter):
        successful = self.drive.change_current_dir(destination_directory)

        if not successful:
            outputter.println(self.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED)

    @staticmethod
    def print_current_directory_path(current_directory_name, outputter):
        outputter.println(current_directory_name)

    def extract_and_check_if_valid_directory(self, dest_dir_name, outputter):
        directory = self.drive.item_from_path(dest_dir_name)

        if directory is None:
            outputter.println(self.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED)
            return None

        if not directory.is_directory():
            outputter.println(self.DESTINATION_IS_FILE)
            return None

        return directory