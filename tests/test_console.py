#!/usr/bin/python3
"""
Unittest for the Console class
Test files by using the following command line:
python3 -m unittest tests/test_console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        with patch('sys.stdin', side_effect=['help', 'quit']):
            self.console.cmdloop()
            self.assertIn('Documented commands (type help <topic>):', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('sys.stdin', side_effect=['create BaseModel', 'quit']):
            self.console.cmdloop()
            self.assertIn('5adebc1c-158d-47c5-898e-b0848897991d', mock_stdout.getvalue())  # Assuming this is the ID generated

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('sys.stdin', side_effect=['create BaseModel', 'show BaseModel 5adebc1c-158d-47c5-898e-b0848897991d', 'quit']):
            self.console.cmdloop()
            self.assertIn('"id": "5adebc1c-158d-47c5-898e-b0848897991d"', mock_stdout.getvalue())  # Assuming this is the ID generated

    # Add more test cases for other commands like update, destroy, etc.

if __name__ == '__main__':
    unittest.main()
s
