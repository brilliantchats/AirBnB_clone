#!/usr/bin/python3
"""
Defines the command interpreter or console for interaction with our objects
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
        }


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
            class_name = args[0]
            if class_name in class_dict.keys():
                model = class_dict[class_name]()
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
                class_name = args[0]
                if class_name in class_dict.keys():
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
                class_name = args[0]
                if class_name in class_dict.keys():
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
            class_name = args[0]
            if class_name in class_dict.keys():
                objs = []
                for k, v in storage.all().items():
                    objs.append(str(v))
                print(objs)
            else:
                print("** class doesn't exist **")
        else:
            objs = []
            dic = storage.all()
            for k, v in dic.items():
                objs.append(str(v))
            print(objs)

    def do_update(self, line=None):
        """Updates an attribute within an object"""
        if line:
            args = line.split()
            class_name = args[0]
            if len(args) >= 4:
                if class_name in class_dict.keys():
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

    def default(self, line):
        """Methods without the do prefix"""
        args = line.split('.')
        class_name = args[0]
        command = args[1].split('(')[0]
        if command == "all":
            objs = storage.all()
            class_arr = []
            for key, value in objs.items():
                name = key.split('.')[0]
                if name == class_name:
                    class_arr.append(str(value))
            print(class_arr)
        elif command == "count":
            objs = storage.all()
            count = 0
            for key, value in objs.items():
                name = key.split('.')[0]
                if name == class_name:
                    count += 1
            print(count)
        elif command == "show":
            iD = args[1][6:(len(args[1]) - 2)]
            string = class_name + " " + iD
            self.do_show(string)
        elif command == "destroy":
            iD = args[1][9:(len(args[1]) - 2)]
            string = class_name + " " + iD
            self.do_destroy(string)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
