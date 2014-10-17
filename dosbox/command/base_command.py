import abc


class BaseCommand(object):
    INCORRECT_SYNTAX = "The syntax of the command is incorrect."
    DEFAULT_ERROR_MESSAGE_WRONG_PARAMETER = "Wrong parameter entered."

    def __init__(self, command_name, drive):
        self.command_name = command_name.lower()
        self.drive = drive
        self._params = list()

    def check_params(self, outputter):
        if not self.check_number_of_params(len(self._params)):
            outputter.println(self.INCORRECT_SYNTAX)
            return False

        if not self.check_param_values(outputter):
            if not outputter.has_characters_printed():
                outputter.println(self.DEFAULT_ERROR_MESSAGE_WRONG_PARAMETER)

            return False

        return True

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        del self._params[:]
        self._params = params

    @abc.abstractmethod
    def check_number_of_params(self, num_of_params):
        return NotImplemented

    @abc.abstractmethod
    def check_param_values(self, outputter):
        return NotImplemented

    @abc.abstractmethod
    def execute(self, outputter):
        return NotImplemented

    def compare(self, command_name):
        return self.command_name == command_name

    def compare_cmd_name(self, cmd_name):
        return True

    def num_of_params(self):
        return len(self._params)

    def param(self, index):
        return self._params[index]

    def __str__(self):
        return self.command_name