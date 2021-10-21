import unittest
from stack import *


class TestStack(unittest.TestCase):

    def test_add(self):
        test_stack = Stack()
        test_stack.add(2)
        test_stack.add(4)
        index = test_stack.index_len()
        size = test_stack.size()
        self.assertEqual(index, size)

    def test_pop(self):
        test_stack = Stack()
        test_stack.add(2)
        test_stack.pop()
        index = test_stack.index_len()
        size = test_stack.size()
        self.assertEqual(index, size)
        test_stack.add(4)
        self.assertEqual(test_stack.pop(), 4)
        self.assertEqual(size, 0)
        self.assertEqual(test_stack.pop(), None)


if __name__ == '__main__':
    unittest.main()
