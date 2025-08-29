import unittest

from greetings import greet

class TestGreetings(unittest.TestCase):

    def test_greet_name(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_no_name(self):
        self.assertEqual(greet(), "Hello, !")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

if __name__ == '__main__':
    unittest.main()
