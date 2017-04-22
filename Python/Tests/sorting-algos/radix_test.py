#!/usr/bin/python3

import unittest
import os
import sys
from random import randint
mod_directory = [os.getcwd() + '/Sorting']
mod_directory.extend(sys.path)
sys.path = mod_directory
from radix import radix_int_sort

class TestSort(unittest.TestCase):
    def test_sort(self):
        for j in range(25):
            array = []
            for i in range(10000):
                array.append(randint(0,1000))
            self.assertListEqual(radix_int_sort(array, 4), sorted(array))

def main():
    insert_sort_suite = unittest.TestLoader().loadTestsFromTestCase(TestSort)
    unittest.TextTestRunner(verbosity=2).run(insert_sort_suite)
