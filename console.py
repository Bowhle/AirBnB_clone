#!/usr/bin/python3
"""Command interpreter for the Airbnb clone."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the Airbnb clone."""

    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a new object of any class."""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show an object by class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, obj_id = args
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Destroy an object by class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, obj_id = args
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_update(self, args):
        """Update an object by class name, id, and attribute."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, obj_id = args[:2]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def do_all(self, args):
        """Show all objects, or all objects of a specific class."""
        if args:
            class_name = args.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            instances = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name
            ]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print("[{}]".format(", ".join(instances)))

    def do_class_all(self, args):
        """Show all instances of a specific class."""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        class_objects = [obj for obj in storage.all().values() if obj.__class__.__name__ == class_name]
        if class_objects:
            instances = [
                f"[{class_name}] ({obj.id}) {obj.to_dict()}" for obj in class_objects
            ]
            print("[{}]".format(", ".join(instances)))
        else:
            print(f"** no instances of class {class_name} found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
