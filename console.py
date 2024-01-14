#!/usr/bin/python3
"""
consol for airbnb project
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ console class iheritaed from cmd"""
    prompt = "(hbnb) "

    cls = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'Place': Place,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

    def emptyline(self):
        """ overrides the empityline command to do nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exits from the console when CTRL + d is pressed"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if line:
            if line in self.cls.keys():
                new_obj = self.cls[line]()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        if line:
            line = line.split()
            if line[0] in self.cls.keys():
                if len(line) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(line[0], line[1])
                storage.reload()
                obj = storage.all()
                if key in obj.keys():
                    print(str(obj[key]))
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        if line:
            line = line.split()
            if line[0] in self.cls.keys():
                if len(line) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(line[0], line[1])
                storage.reload()
                obj = storage.all()
                if key in obj.keys():
                    del obj[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        if line:
            line = line.split()
            if line[0] in self.cls.keys():
                if len(line) < 2:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(line[0], line[1])
                storage.reload()
                obj = storage.all()
                if key in obj.keys():
                    if len(line) < 3:
                        print("** attribute name missing **")
                        return
                    if len(line) < 4:
                        print("** value missing **")
                        return
                    setattr(obj[key], line[2], line[3])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")

    def do_all(self, line):
        """ Prints all string representation
        of all instances based or not on the class name"""
        list_obj = []
        storage.reload()
        objt = storage.all()
        if line:
            if line in self.cls.keys():
                for key, value in objt.items():
                    class_name, objt_id = key.split(".")
                    if line == class_name:
                        list_obj.append(str(value))
                print(list_obj)
                return
            else:
                print("** class doesn't exist **")
                return
        for key, value in objt.items():
            list_obj.append(str(value))
        print(list_obj)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
