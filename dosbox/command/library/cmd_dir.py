from dosbox.command.framework.command import *


class CmdDir(Command):
    SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED = "File Not Found."

    def __init__(self, name, drive):
        super().__init__(name, drive)
        self.directory_to_print = None

    def check_number_of_params(self, num_of_params):
        return num_of_params == 0 or num_of_params == 1

    def check_param_values(self, outputter):
        if self.params_count() == 0:
            self.directory_to_print = self.drive.current_dir
        else:
            self.directory_to_print = self.check_and_prepare_path_param(self.params[0], outputter)

        return self.directory_to_print is not None

    def check_and_prepare_path_param(self, path_name, outputter):
        file_system_item = self.drive.item_from_path(path_name)

        if file_system_item is None:
            outputter.println(self.SYSTEM_CANNOT_FIND_THE_PATH_SPECIFIED)
            return

        if not file_system_item.is_directory():
            return file_system_item.parent

        return file_system_item

    def execute(self, outputter):
        if self.directory_to_print is not None:
            self.print_header(self.directory_to_print, outputter)
            self.print_content(self.directory_to_print.content, outputter)
            self.print_footer(self.directory_to_print, outputter)

    @staticmethod
    def print_header(directory_to_print, outputter):
        outputter.println("Directory of " + directory_to_print.path())
        outputter.newline()

    @staticmethod
    def print_content(directory_content, outputter):
        for item in directory_content:
            if item.is_directory():
                outputter.print("<DIR>")
            else:
                outputter.print( str(item.size()) )

            outputter.print("\t" + item.name)
            outputter.newline()

    @staticmethod
    def print_footer(directory_to_print, outputter):
        outputter.println("\t" + str(directory_to_print.number_of_contained_files()) + " File(s)");
        outputter.println("\t" + str(directory_to_print.number_of_contained_directories()) + " Dir(s)");

