from django.test import SimpleTestCase

from app import caltest
class CalscTest(SimpleTestCase):
    def test_add(self):
        res = caltest.add(2,3)
        
        self.assertEqual(res,10)