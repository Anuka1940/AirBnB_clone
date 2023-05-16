#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    # public class attributes
    prompt = '(hbnb)'

    def do_quit(self, arg):
        '''Quit command to exit the interpreter'''
        return True

    def do_EOF(self, arg):
        '''EOF command to exit the interpreter'''
        return True

    def emptyline(self):
        '''Do nothing when called'''
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
