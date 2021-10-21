import unittest
from queue_two import *


class TestQueueTwo(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(3)
        self.assertEqual(queue.size(), 1)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 2)


if __name__ == "__main__":
    unittest.main()
