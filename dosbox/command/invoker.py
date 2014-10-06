import re


class Invoker:
    WRONG_PARAMETER_ERR = "Wrong parameter entered."

    def __init__(self):
        self.commands = list()

    def add_command(self, command):
        self.commands.append(command)

    def parse_command_name(self, name):
        command = name.lower().strip()
        command = re.sub('[,;]', " ", command)

        cmd = command
        for i in range(0, len(command)):
            if command[i] == " ":
                cmd = command[0:i]
                break

        return cmd

    def parse_command_params(self, command):
        params = list()

        cmd = command.lower().strip()
        cmd = re.sub('[,;]', " ", cmd)

        last_space = 0
        for i in range(0, len(cmd)):
            if cmd[i] == " " or i+1 == len(cmd):
                params.append(cmd[last_space:i+1].strip())
                last_space = i

        # Check if params is empty
        if params:
            params.pop(0)  # Remove command
            params = [param for param in params if param]  # Clean out empty string

        return params

    def execute_command(self, command, outputter):
        command_name = self.parse_command_name(command)
        params = self.parse_command_params(command)

        try:
            for cmd in self.commands:
                if cmd.compare(command_name):
                    cmd.params = params

                    if not cmd.check_params(outputter):
                        # outputter.println(self.WRONG_PARAMETER_ERR)
                        return

                    cmd.execute(outputter)
                    return

            outputter.println("%(command)s is not recognized as an internal or external command, operable program or batch file." % \
                              {"command": command_name})
        except Exception as e:
            print(e)