#!/usr/bin/python

import unittest
import math
execfile('./Dynamic Programming/edit-distance.py')


class TestEDDP(unittest.TestCase):

    def test_edit_distance_dp(self):
        self.assertEqual(edit_distance('ab', 'ab'), 0)
        self.assertEqual(edit_distance('aaa', ''), 3)
        self.assertEqual(edit_distance('aba', 'aaa'), 1)
        self.assertEqual(edit_distance('abca', 'aaa'), 2)
        self.assertEqual(edit_distance('abca', 'eaaga'), 3)
        self.assertEqual(edit_distance('distance', 'editing'), 5)
        self.assertEqual(edit_distance('hamburger', 'hot dog'), 7)
        self.assertEqual(edit_distance('republican', 'democrat'), 8)
        self.assertEqual(edit_distance(
            'sally sells sea shells down by the sea shore', 'the sixth slick sheik\'s sheep is sick'), 33)


ed_test_suite = unittest.TestLoader().loadTestsFromTestCase(TestEDDP)
unittest.TextTestRunner(verbosity=2).run(ed_test_suite)
