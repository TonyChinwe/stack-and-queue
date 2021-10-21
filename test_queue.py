import unittest
from queue import *


class TestQueue(unittest.TestCase):

    def test_enque(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), None)


if __name__ == "__main__":
    unittest.main()
