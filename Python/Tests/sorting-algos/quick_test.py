#!/usr/bin/python3

import unittest
import os
import sys
from random import randint
mod_directory = [os.getcwd() + '/Sorting']
mod_directory.extend(sys.path)
sys.path = mod_directory
from quick import qsort, qsort_inplace

class TestSort(unittest.TestCase):
    def test_sort(self):
        for j in range(25):
            array = []
            for i in range(1000):
                array.append(randint(-100,100))
            self.assertListEqual(qsort(array), sorted(array))

    def test_sort_inplace(self):
        for j in range(25):
            array = []
            for i in range(1000):
                array.append(randint(-100,100))
            self.assertListEqual(qsort_inplace(array), sorted(array))

def main():
    insert_sort_suite = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner(verbosity=2).run(insert_sort_suite)
