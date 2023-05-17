#!/usr/bin/python3
''' Define unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_Instance
    TestBaseModel_Save
    TestBaseModel_To_Dict
'''
import unittest
from datetime import datetime
from unittest.mock import patch
from  models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        expected_output = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_output)

    def test_save(self):
        bm = BaseModel()
        updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertLess(updated_at, bm.updated_at)

    def test_to_dict(self):
        expected_dict = {
            "__class__": "BaseModel",
            "id": self.base_model.id,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat(),
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
