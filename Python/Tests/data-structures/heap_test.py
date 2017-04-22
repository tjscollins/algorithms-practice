import unittest
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from heap import Heap
from random import randint

class TestHeapMethods(unittest.TestCase):

    def test_build_heaps(self):
        array = []
        for i in range(10000):
            array.append(randint(-100, 100))
        newHeap = Heap(array, 'max')
        self.assertTrue(check_heap_prop(newHeap.array, newHeap.type))
        newHeap = Heap(array, 'min')
        self.assertTrue(check_heap_prop(newHeap.array, newHeap.type))

    def test_heap_sort(self):
        array = []
        for i in range(10000):
            array.append(randint(-100, 100))
        newHeap = Heap(array, 'max')
        array.sort(key=int)
        self.assertListEqual(newHeap.heapSort(), array)
        newHeap = Heap(array, 'min')
        array.reverse()
        self.assertListEqual(newHeap.heapSort(), array)

def main():
    heapMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestHeapMethods)
    unittest.TextTestRunner(verbosity=2).run(heapMethodSuite)

def check_heap_prop(arr, type):
    for i in range(len(arr) // 2 - 2):
        if type == 'max' and (arr[2*i + 1] > arr[i] or arr[2*i+2] > arr[i]):
            print(type, arr[i], arr[2*i+1], arr[2*i+2])
            return False
        elif type == 'min' and (arr[2*i + 1] < arr[i] or arr[2*i+2] < arr[i]):
            print(type, arr[i], arr[2*i+1], arr[2*i+2])
            return False
    return True
