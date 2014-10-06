import abc

class FileSystemItem(object):
    ILLEGAL_ARGUMENT_TEXT = "Error: A file or directory name may not contain '/', '\', ',', ' ' or ':'"

    def __init__(self, name, parent):
        if not self.check_name(name):
            raise(Exception(self.ILLEGAL_ARGUMENT_TEXT))

        self.name = name
        self.parent = parent

    # Check name
    def check_name(self, name):
        if "\\" in name or "/" in name or "," in name or " " in name:
            return False

        return True

    def name(self, name):
        if not self.check_name(name):
            raise(Exception(self.ILLEGAL_ARGUMENT_TEXT))

    def path(self):
        if self.parent is not None:
            return self.parent.path() + "\\" + self.name
        else:
            # Root directory
            return self.name

    @abc.abstractmethod
    def is_directory(self):
        return NotImplemented

    @abc.abstractmethod
    def number_of_contained_files(self):
        return NotImplemented

    @abc.abstractmethod
    def number_of_contained_directories(self):
        return NotImplemented

    @abc.abstractmethod
    def size(self):
        return NotImplemented

    def __str__(self):
        return self.path()