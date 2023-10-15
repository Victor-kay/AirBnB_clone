#!/usr/bin/python3
"""
HBNB console
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

# Define a set of valid classes
classes = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Place",
    "Amenity",
    "Review"
}


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    # Set the command prompt
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Handle an empty line by doing nothing.
        """
        pass

    def default(self, arg):
        """
        Handle default behavior when an invalid command is entered.
        """
        command_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            arg_list = arg.split('.')
            if len(arg_list) == 2:
                method = arg_list[1].split("(")[0]
                arguments = arg_list[1].split("(")[1][:-1]
                if method in command_dict:
                    new_command = "{} {}".format(arg_list[0], arguments)
                    return command_dict[method](new_command)
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """
        Handle the quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle the EOF signal to exit the program.
        """
        print()
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class, save it, and print its id.
        """
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Display the string representation of an instance.
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[key]
                storage.save()

    def do_all(self, arg):
        """
        Display string representations of instances.
        """
        arg_list = parse(arg)
        if not arg_list:
            objects = storage.all()
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            objects = storage.all(arg_list[0])

        print([str(obj) for obj in objects.values()])

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.
        """
        arg_list = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Update a class instance based on the class name and id.
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if not arg_list:
            print("** class name missing **")
            return
        if arg_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return

        obj = obj_dict[key]
        if len(arg_list) == 4:
            if arg_list[2] in obj.__class__.__dict__:
                val_type = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = val_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            for k, v in eval(arg_list[2]).items():
                if k in obj.__class__.__dict__ and type(obj.__class__.__dict__[k]) in (str, int, float):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
