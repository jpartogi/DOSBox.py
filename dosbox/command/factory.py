from dosbox.command.library.cmd_dir import *
from dosbox.command.library.cmd_mk_dir import *
from dosbox.command.library.cmd_mk_file import *
from dosbox.command.library.cmd_cd import *

class Factory(object):
    def __init__(self, drive):
        self.drive = drive
        self.commands = list()

        self.commands.append(CmdDir("dir", drive))
        self.commands.append(CmdMkDir("mkdir", drive))
        self.commands.append(CmdMkFile("mkfile", drive))
        self.commands.append(CmdCd("cd", drive))