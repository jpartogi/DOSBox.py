from dosbox.filesystem.file_system_item import *

class Directory(FileSystemItem):
    def __init__(self, name):
        super().__init__(name, None)
        self.content = list()

    def add(self, file_system_item):
        self.content.append(file_system_item)

        if not self.has_another_parent(file_system_item):
            self.remove_parent(file_system_item)

        file_system_item.parent = self

    def remove(self, file_system_item):
        if file_system_item in self.content:
            file_system_item.parent = None
            self.content.remove(file_system_item)

    def has_another_parent(self, file_system_item):
        return file_system_item.parent is None

    def remove_parent(self, file_system_item):
        file_system_item.parent = None

    def is_directory(self):
        return True

    def num_of_contained_files(self):
        number_of_files = 0

        for item in self.content:
            if not item.is_directory():
                number_of_files += 1

        return number_of_files

    def num_of_contained_dirs(self):
        number_of_dirs = 0

        for item in self.content:
            if item.is_directory():
                number_of_dirs += 1

        return number_of_dirs

    def size(self):
        return 0