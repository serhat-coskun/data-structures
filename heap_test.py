import unittest
from heap import Heap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap(lambda parent, child: parent < child)

    def test_add(self):
        self.heap.add(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(2)
        self.assertEqual(self.heap.peek(), 2)
        self.heap.add(7)
        self.assertEqual(self.heap.peek(), 2)

    def test_pop(self):
        self.heap = Heap(
            lambda parent, child: parent < child,
            collection=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0],
        )
        self.assertEqual(self.heap.pop(), 0)
        self.assertEqual(self.heap.pop(), 1)
        self.assertEqual(self.heap.pop(), 2)

    def test_peek_empty(self):
        with self.assertRaises(Exception):
            self.heap.peek()

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.heap.pop()

    def test_add_pop_mix(self):
        self.heap.add(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(2)
        self.assertEqual(self.heap.peek(), 2)
        self.heap.add(7)
        self.assertEqual(self.heap.peek(), 2)
        self.assertEqual(self.heap.pop(), 2)
        self.assertEqual(self.heap.pop(), 5)
        self.assertEqual(self.heap.pop(), 7)

    def test_len(self):
        for i in range(9):
            self.heap.add(i)

        self.assertEqual(len(self.heap), 9)

    def test_empty_truthiness(self):
        self.assertFalse(self.heap)

    def test_nonempty_truthiness(self):
        self.heap = Heap(collection=[0, 0, 0])
        self.assertTrue(self.heap)


class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap(lambda parent, child: parent > child)

    def test_add(self):
        self.heap.add(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(2)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(7)
        self.assertEqual(self.heap.peek(), 7)

    def test_pop(self):
        self.heap = Heap(
            inOrderFunc=lambda parent, child: parent > child,
            collection=[1, 3, 5, 7, 9, 2],
        )
        self.assertEqual(self.heap.pop(), 9)
        self.assertEqual(self.heap.pop(), 7)
        self.assertEqual(self.heap.pop(), 5)

    def test_add_pop_mix(self):
        self.heap.add(5)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(2)
        self.assertEqual(self.heap.peek(), 5)
        self.heap.add(7)
        self.assertEqual(self.heap.peek(), 7)
        self.assertEqual(self.heap.pop(), 7)
        self.assertEqual(self.heap.pop(), 5)
        self.assertEqual(self.heap.pop(), 2)

    def test_peek_empty(self):
        with self.assertRaises(Exception):
            self.heap.peek()

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.heap.pop()

    def test_len(self):
        for i in range(9):
            self.heap.add(i)

        self.assertEqual(len(self.heap), 9)

    def test_truthiness(self):
        self.assertFalse(self.heap)

    def test_nonempty_truthiness(self):
        self.heap = Heap(collection=[0, 0, 0])
        self.assertTrue(self.heap)


if __name__ == "__main__":
    unittest.main()
