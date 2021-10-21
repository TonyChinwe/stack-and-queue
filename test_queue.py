import unittest
from queue import *


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        pass

    def test_enque(self):
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 2)

    def test_dequeue(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), None)


if __name__ == "__main__":
    unittest.main()
