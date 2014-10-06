from dosbox.filesystem.directory import *

class Drive:
    def __init__(self, drive_letter):
        self.drive_letter = drive_letter.upper()
        self.drive_letter_colon = self.drive_letter + ":"
        self.label = ""
        self.root_dir = Directory(self.drive_letter_colon)
        self.current_dir = self.root_dir

    def restore(self):
        return NotImplemented

    def save(self):
        return NotImplemented

    def create_from_real_dir(self, path):
        return NotImplemented

    def change_current_dir(self, dir):
        if self.item_from_path(dir.path()) == dir:
            self.current_dir = dir
            return True
        else:
            return False

    def item_from_path(self, item_path):
        # Replace any "/" with "\"
        item_path = item_path.replace("/", "\\").strip()

        # Remove '\' from the end of the path
        if item_path[len(item_path)-1] == "\\" and len(item_path) >= 2:
            item_path = item_path[0:len(item_path)-1]

        if item_path == "\\":
            return self.root_dir

        # Check for ..\
        if len(item_path) >= 3 and "..\\" in item_path:
            item_path = self.current_dir.parent.path() + "\\" + item_path[3:len(item_path)]

        # Check for .\
        if len(item_path) >= 2 and ".\\" in item_path:
            item_path = item_path[1:len(item_path)]

        if item_path == '..':
            parent = self.current_dir.parent
            if parent is None:
                parent = self.root_dir

            return parent

        if item_path == '.':
            return self.current_dir

        # Add drive name if path starts with "\"
        if item_path and item_path[0] == "\\":
            item_path = self.drive_letter + ":" + item_path

        # Make absolute path from relative paths
        if len(item_path) == 1 or ':' not in item_path:
            item_path = self.current_dir.path() + "\\" + item_path

        # Find more complex paths recursively
        if item_path == self.root_dir.path():
            return self.root_dir

        return self.item_from_dir(item_path, self.root_dir)

    def item_from_dir(self, item_name, dir):
        content = dir.content

        for item in content:
            path = item.path()

            if path.lower() == item_name.lower():
                return item

            if item.is_directory():
                value = self.item_from_dir(item_name, item)
                if value is not None:
                    return value

        return None

    def prompt(self):
        return self.current_dir.path() + "\>"

    def drive_letter(self):
        return self.drive_letter + ":"

    def __str__(self):
        return self.drive_letter
