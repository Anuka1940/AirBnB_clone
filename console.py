#!/usr/bin/python3
'''import cammand interpreter'''
import shlex
from cmd import Cmd
from models.base_model import BaseModel
from models import storage
from models.user import Uetr
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
clist = storage.models


class HBNBCommand(Cmd):
    '''Start command processing'''

    # public class attributes
    prompt = '(hbnb)'
    cmds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_quit(self, arg):
        '''Quit command to exit the interpreter'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the interpreter'''
        return True

    def emptyline(self):
        '''Do nothing when called'''
        pass

    def do_create(self, args):
        ''' Create a new instance of BaseModel'''
        args, num = parse(args, ' ')

        if not args:
            print("** class name missing **")
        elif args[0] not in clist:
            print("** class doesn't exist **")
        elif num == 1:
            tmp = eval(args[0])()
            print(tmp.id)
            tmp.save()
        else:
            print("** Too many arguments for create **")
            pass

    def do_show(self, args):
        args, num = parse(args, ' ')

        if not args:
            print("** class name missing **")
        class_name = args[0]
        if args[0] not in clist:
            print("** class doesn't exist **")
        elif num < 2:
            print("** instance id missing **")
        instance_id = args[1]
        instance = storage.get_instance(class_name, instance_id)
        if not instance:
            print("** no instance found **")
        print(instance)

    def do_destroy(self, args):
        args, num = parse(args, ' ')

        if not args:
            print("** class name missing **")
        class_name = args[0]
        if args[0] not in clist:
            print("** class doesn't exist **")
        elif num < 2:
            print("** instance id missing **")
        if num == 2:
            storage.delete_by_id(*args)
        else:
            print("** no instance found **")

    def do_all(self, args):
        args, num = parse(args, ' ')

        if num < 2:
            print(storage.get_all(*args))
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, args):
        '''Update an instance base on the class name and id'''
        args, num = parse(args, ' ')

        if not num:
            print("** class name missing **")
        elif args[0] not in clist:
            print("** class doesn't exist **")
        elif num == 1:
            print("** instance id missing **")
        elif num == 2:
            print("** attribute name missing **")
        elif num == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            if attribute_name not in ['id', 'created_at', 'updated_at']:
                instance = storage.get_instance(class_name, instance_id)
                if instance:
                    setattr(instance, attribute_name, eval(attribute_value))
                    instance.save()
                else:
                    print("** no instance found **")
            else:
                print("** attribute name cannot be updated **")


def parse(args, sep):
    '''
        Parses the command line arguments base on the provided delimeterl.
        Args:
        args(list): list of cammand line arguments.
        delimeter(str): comma and space.

        Returns: A tuple of list of arguments and numbers
    '''
    parsed_args = []
    for arg in args.split(sep):
        parsed_args.append(arg)
    return parsed_args, len(parsed_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
