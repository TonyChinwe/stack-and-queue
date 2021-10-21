import unittest
from stack_two import *


class TestStackTwo(unittest.TestCase):

    def test_append(self):
        test_stack = StackTwo()
        test_stack.append(2)
        self.assertEqual(test_stack.pop(), 2)

    def test_pop(self):
        test_stack = StackTwo()
        test_stack.append(3)
        self.assertEqual(test_stack.pop(), 3)


if __name__ == "__main__":
    unittest.main()
