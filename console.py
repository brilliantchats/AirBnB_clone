#!/usr/bin/python3
"""
Defines the command interpreter or console for interaction with our objects
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class to define entry point for console
    """
    prompt = "(hbnp) "

    def do_EOF(self, line):
        """Exits the console"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Does nothing when an empty line+ enter is given"""
        pass

    def do_create(self, line=None):
        """Creates a BaseModel instance"""
        if line:
            args = line.split()
            if args[0] == "BaseModel" or args[0] == "User":
                if args[0] == "BaseModel":
                    model = BaseModel()
                else:
                    model = User()
                print(model.id)
                model.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line=None):
        """Prints the str representation of a BaseModel based on class, id"""
        if line:
            args = line.split()
            if len(args) == 2:
                if args[0] == "BaseModel" or args[0] == "User":
                    objs = storage.all()
                    for key, value in objs.items():
                        iD = key.split('.')[1]
                        if iD == args[1]:
                            print(value)
                            return
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line=None):
        """Destroys an instance based on class name and id"""
        if line:
            args = line.split()
            if len(args) == 2:
                if args[0] == "BaseModel" or args[0] == "User":
                    objs = storage.all()
                    for key, value in objs.items():
                        iD = key.split('.')[1]
                        if iD == args[1]:
                            del storage.all()[key]
                            storage.save()
                            return
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line=None):
        """Prints all str implementation of instances"""
        if line:
            args = line.split()
            if args[0] == "BaseModel" or args[0] == "User":
                objs = []
                for k, v in storage.all().items():
                    objs.append(str(v))
                print(objs)
            else:
                print("** class doesn't exist **")
        else:
            objs = []
            for k, v in storage.all().items():
                objs.append(str(v))
            print(objs)

    def do_update(self, line=None):
        """Updates an attribute within an object"""
        if line:
            args = line.split()
            if len(args) >= 4:
                if args[0] == "BaseModel" or args[0] == "User":
                    objs = storage.all()
                    for k, v in objs.items():
                        iD = k.split('.')[1]
                        if iD == args[1]:
                            setattr(storage.all()[k],
                                    args[2], type(args[2])(args[3]))
                            storage.save()
                            return
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
