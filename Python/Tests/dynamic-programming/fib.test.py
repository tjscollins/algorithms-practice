#!/usr/bin/python

import unittest
import math
execfile('./Dynamic Programming/fibonacci.py')


def quick_fib(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n - (-phi)**(-n)) / math.sqrt(5))


class TestFibDP(unittest.TestCase):

    def test_fib_dp(self):
        for i in range(2, 70, 1):
            self.assertEqual(fib(i), quick_fib(i))

fib_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFibDP)
unittest.TextTestRunner(verbosity=2).run(fib_test_suite)
