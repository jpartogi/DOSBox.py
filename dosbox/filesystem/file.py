from dosbox.filesystem.file_system_item import *

class File(FileSystemItem):
    def __init__(self, name, content):
        super().__init__(name, None)
        self.content = content

    def is_directory(self):
        return False

    def num_of_contained_files(self):
        return 0

    def num_of_contained_dirs(self):
        return 0

    def size(self):
        return len(self.content)