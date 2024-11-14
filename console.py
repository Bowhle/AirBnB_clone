#!/usr/bin/python3
"""This program contains the entry point for the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """The command line interface for the AirBnB clone."""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit the program when EOF is reached."""
        return True

    def do_quit(self, line):
        """Quit the program."""
        return True

    def emptyline(self):
        """Override to do nothing when an empty line is entered."""
        return False

    def do_create(self, args):
        """Create a new instance of BaseModel, save it, and print its ID."""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

