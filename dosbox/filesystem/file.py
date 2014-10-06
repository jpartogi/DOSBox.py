from dosbox.filesystem.file_system_item import *

class File(FileSystemItem):
    def __init__(self, name, content):
        super().__init__(name, None)
        self.content = content

    def is_directory(self):
        return False

    def number_of_contained_files(self):
        return 0

    def number_of_contained_directories(self):
        return 0

    def size(self):
        return len(self.content)