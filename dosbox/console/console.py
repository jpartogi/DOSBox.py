from sys import stdin

from dosbox.console.console_outputter import *

class Console(object):
    def __init__(self, invoker, drive, outputter):
        self.invoker = invoker
        self.drive = drive
        self.outputter = outputter

    def process_input(self):
        self.outputter.println("DOSBox, Scrum.org, Professional Scrum Developer Training.")
        self.outputter.println("Copyright (c) Joshua Partogi. All rights reserved.")

        lines = ""

        while lines != "exit":
            self.outputter.newline()
            self.outputter.print(self.drive.prompt())

            try:
                chars = stdin.readline()

                lines = str(chars).strip()
            except Exception as e:
                break

            self.outputter.reset_statistics()
            self.invoker.execute_command(lines, self.outputter)

        print("Goodbye!")
        self.drive.save()