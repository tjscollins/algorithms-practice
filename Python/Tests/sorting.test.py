#!/usr/bin/python
import unittest
execfile('Sorting/counting-sort/csort.py')
execfile('Sorting/radix-sort/radix.py')
execfile('Sorting/selection-sort/select-sort.py')
execfile('Sorting/merge-sort/merge-sort.py')
execfile('Sorting/quick-sort/quick-sort.py')
execfile('Sorting/quick-sort/quick-sort-inplace.py')


class TestSortingMethods(unittest.TestCase):

    def test_select_sort(self):
        self.assertListEqual(select_sort([3, 2, 1]), [1, 2, 3])
        self.assertListEqual(select_sort([3, 2, 1, 9, 8, 4, 5, 7, 6]), [
                             1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(select_sort(
            [-1, 0, 0, -1, -2, -3, 10, 9, 8, 7, -6, -5, -4]), [-6, -5, -4, -3, -2, -1, -1, 0, 0, 7, 8, 9, 10])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([10, 100, 320, -5, 6, 9, 100, -25, 4, 8, 5, 4,
                                     6, 9, 0, 7]), [-25, -5, 0, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10, 100, 100, 320])
        self.assertEqual(merge_sort([1, 4, 8, 5, 4, 6, 9, 0, 7]), [
                         0, 1, 4, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort([0]), [0])

    def test_qsort(self):
        self.assertEqual(qsort([0]), [0])
        self.assertEqual(qsort([100, -1000, 1, 3, 3, 3, 2, 1, 1, 100, 200, 300]),
                         [-1000, 1, 1, 1, 2, 3, 3, 3, 100, 100, 200, 300])
        self.assertEqual(qsort([1, 1, 1, 1, 2, 1, 1, 1, 3, 4]), [
                         1, 1, 1, 1, 1, 1, 1, 2, 3, 4])

    def test_qsort_inplace(self):
        self.assertEqual(qsort_inplace([0]), [0])
        self.assertEqual(qsort_inplace(
            [100, -1000, 1, 3, 3, 3, 2, 1, 1, 100, 200, 300]), [-1000, 1, 1, 1, 2, 3, 3, 3, 100, 100, 200, 300])
        self.assertEqual(qsort_inplace([1, 1, 1, 1, 2, 1, 1, 1, 3, 4]), [
                         1, 1, 1, 1, 1, 1, 1, 2, 3, 4])

    def test_csort(self):
        self.assertEqual(csort([5, 4, 3, 5, 3, 2, 1, 2, 1], [1, 5]), [
                         1, 1, 2, 2, 3, 3, 4, 5, 5])
        self.assertEqual(csort([2, 3, 3, 1], [1, 3]), [1, 2, 3, 3])
        self.assertEqual(csort([10, 3, 2, 1, 3, 2, 1, 10], [1, 10]), [
                         1, 1, 2, 2, 3, 3, 10, 10])

    def test_csort_radix(self):
        self.assertListEqual(csort_radix(
            [[9, 99], [9, 89], [1, 91]], [0, 9]), [91, 99, 89])
        self.assertListEqual(csort_radix(
            [[1, 11], [2, 2], [0, 100]], [0, 9]), [100, 11, 2])

    def test_radix(self):
        self.assertListEqual(radix_int_sort([987, 989, 981, 324, 435, 789, 167, 614], 3), [
                             167, 324, 435, 614, 789, 981, 987, 989])
        self.assertListEqual(radix_int_sort([9873, 4367, 659, 2670, 234], 4), [
                             234, 659, 2670, 4367, 9873])
        self.assertListEqual(radix_int_sort([123456789, 87654321, 2345678, 765432, 34567, 6543, 456, 65, 5], 10), [
                             5, 65, 456, 6543, 34567, 765432, 2345678, 87654321, 123456789])

sortMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestSortingMethods)
unittest.TextTestRunner(verbosity=2).run(sortMethodSuite)
