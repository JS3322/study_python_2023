import unittest
from ctypes import cdll

class TestStringMethods(unittest.TestCase):
    

    def test_print(self):
        lib = cdll.LoadLibrary("lib/libinit_test.dylib")
        print("__________check_A")
        lib.on_test()
        print("__________check_B")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()