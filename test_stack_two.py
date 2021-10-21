import unittest
from stack_two import *


class TestStackTwo(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("Setting up the class")

    # @classmethod
    # def tearDownClass(cls):
    #     print("Tearing down class")

    def setUp(self):
        self.test_stack = StackTwo()

    def tearDown(self):
        pass

    def test_append(self):
        self.test_stack.append(2)
        self.assertEqual(self.test_stack.pop(), 2)

    def test_pop(self):
        self.test_stack.append(3)
        self.assertEqual(self.test_stack.pop(), 3)


if __name__ == "__main__":
    unittest.main()
