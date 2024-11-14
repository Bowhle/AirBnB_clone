#!/usr/bin/python3
"""This program contains the entry point for the command interpreter."""
import cmd
from models.base_model import BaseModel
from models.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """The command line interface for the AirBnB clone."""
    prompt = '(hbnb) '
    storage = FileStorage()
    storage.reload()  # Load data from file

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
        """Create a new instance of BaseModel (or any valid class), save it, and print its ID."""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:  # Add all valid class names here
            print("** class doesn't exist **")
            return
        else:
            # Create an instance dynamically based on the class name
            class_name = args[0]
            new_instance = globals()[class_name]()  # Instantiate the class dynamically
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Print the string representation of an instance based on the class name and id."""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in self.storage.all():
                print(self.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in self.storage.all():
                del self.storage.all()[key]
                self.storage.save()  # Save changes to the JSON file
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        if len(args) == 0:
            result = [str(obj) for obj in self.storage.all().values()]
            print(f"[{', '.join(result)}]")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            result = [str(obj) for key, obj in self.storage.all().items() if key.startswith(class_name)]
            print(f"[{', '.join(result)}]")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating an attribute."""
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            value = args[3]

            key = f"{class_name}.{instance_id}"
            if key not in self.storage.all():
                print("** no instance found **")
                return

            instance = self.storage.all()[key]

            # Cast the value to the correct type
            if hasattr(instance, attribute_name):
                attr_type = type(getattr(instance, attribute_name))
                if attr_type == str:
                    value = str(value)
                elif attr_type == int:
                    value = int(value)
                elif attr_type == float:
                    value = float(value)
                setattr(instance, attribute_name, value)
                instance.save()
            else:
                print(f"** attribute {attribute_name} not found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
