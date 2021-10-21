import unittest
from stack import *


class TestStack(unittest.TestCase):

    def setUp(self):
        self.test_stack = Stack()

    def tearDown(self):
        pass

    def test_add(self):
        self.test_stack.add(4)
        index = self.test_stack.index_len()
        size = self.test_stack.size()
        self.assertEqual(index, size)

    def test_pop(self):
        self.test_stack.pop()
        index = self.test_stack.index_len()
        size = self.test_stack.size()
        self.assertEqual(index, size)
        self.test_stack.add(4)
        self.assertEqual(self.test_stack.pop(), 4)
        self.assertEqual(size, 0)
        self.assertEqual(self.test_stack.pop(), None)


if __name__ == '__main__':
    unittest.main()
