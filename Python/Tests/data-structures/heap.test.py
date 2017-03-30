#!/usr/bin/python3
import unittest
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from heap import Heap

class TestHeapMethods(unittest.TestCase):

    def test_build_heaps(self):
        newHeap = Heap([3, 2, 1, 5, 6, 4], 'max')
        self.assertListEqual(newHeap.array, [6, 5, 4, 3, 2, 1])
        newHeap = Heap([3, 2, 1, 5, 6, 4], 'min')
        self.assertListEqual(newHeap.array, [1, 2, 3, 5, 6, 4])

    def test_heap_sort(self):
        newHeap = Heap([1, 2, -1, 5, 10, 13, -3, 25, 12], 'max')
        self.assertListEqual(newHeap.heapSort(),
                             [-3, -1, 1, 2, 5, 10, 12, 13, 25])
        newHeap = Heap([1, 2, -1, 5, 10, 13, -3, 25, 12], 'min')
        self.assertListEqual(newHeap.heapSort(), [
                             25, 13, 12, 10, 5, 2, 1, -1, -3])

heapMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestHeapMethods)
unittest.TextTestRunner(verbosity=2).run(heapMethodSuite)
