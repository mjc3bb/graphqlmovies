from django.test import TestCase
from .query import schema
from .models import UserModel
import json


class APITest(TestCase):

    def setUp(self) -> None:
        self.schema = schema

    def test_call_executes(self):
        a = UserModel(name='Caleb', last_name='Widowgast')
        a.full_clean()
        a.save()
        l = self.schema.execute('''
        query{
            users{
                name
                lastName
            }
        }
        ''')
        print(json.dumps(l.data, indent=4))

