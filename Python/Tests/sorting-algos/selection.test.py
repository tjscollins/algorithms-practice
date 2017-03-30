#!/usr/bin/python

import unittest
execfile('./Sorting/selection-sort/select-sort.py')

class TestSelectSort(unittest.TestCase):
    def test_select_sort(self):
        self.assertListEqual(select_sort([3,2,1]), [1,2,3])
        self.assertListEqual(select_sort([3,2,1,9,8,4,5,7,6]), [1,2,3,4,5,6,7,8,9])
        self.assertListEqual(select_sort([-1,0,0,-1,-2,-3,10,9,8,7,-6,-5,-4]), [-6,-5,-4,-3,-2,-1,-1,0,0,7,8,9,10])
        self.assertListEqual(select_sort([-4,-1,8,-3,5,-6,0,1,5,6,-2,8,9,-7,-9,6,-3,-2,-9,-8,-6,1,-1,0,-8,-7,2,4,-5,-5,-4,4,7,2,3,3,7,9]), [-9,-9,-8,-8,-7,-7,-6,-6,-5,-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9])

select_sort_suite = unittest.TestLoader().loadTestsFromTestCase(TestSelectSort)
unittest.TextTestRunner(verbosity=2).run(select_sort_suite)
