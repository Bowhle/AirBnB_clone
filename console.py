#!/usr/bin/python3
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
    """Command interpreter for the Airbnb clone."""
    prompt = "(hbnb) "

    # Create new object
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

    # Show object by class and id
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

    # Destroy object by class and id
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

    # Update object by class, id, and attribute
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

    # Show all objects
    def do_all(self, args):
        """Show all objects, or all objects of a specific class."""
        if args:
            class_name = args.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            instances = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == class_name]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print("[{}]".format(", ".join(instances)))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
