class ConsoleOutputter:
    number_of_printed_chars = 0

    def println(self, text):
        print(text)
        self.analyse_printed_chars(text)

    def newline(self):
        print("\n")

    def print(self, text):
        print(text, end="", flush=True)
        self.analyse_printed_chars(text)

    def has_characters_printed(self):
        return self.number_of_printed_chars > 0

    def analyse_printed_chars(self, text):
        self.number_of_printed_chars += len(text.strip())

    def reset_statistics(self):
        self.number_of_printed_chars = 0