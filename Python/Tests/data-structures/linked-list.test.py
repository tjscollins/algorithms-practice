#!/usr/bin/python3
import unittest
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from linkedlist import LinkList


class TestLinkListMethods(unittest.TestCase):

    def test_insert(self):
        newlist = LinkList()
        newlist.insert(1)
        newlist.insert(2)
        self.assertEqual(newlist.head.value, 2)
        self.assertEqual(newlist.head.next.value, 1)

    def test_remove(self):
        newlist = LinkList()
        newlist.insert(1)
        newlist.insert(2)
        self.assertEqual(newlist.head.value, 2)
        newlist.remove()
        self.assertEqual(newlist.head.value, 1)

    def test_traverse(self):
        newlist = LinkList()
        newlist.insert(1)
        newlist.insert(2)
        newlist.insert(10)
        newlist.insert(200)
        self.assertEqual(newlist.traverse(), [200, 10, 2, 1])

    def test_search(self):
        newlist = LinkList()
        newlist.insert(1)
        newlist.insert(2)
        newlist.insert(10)
        newlist.insert(200)
        self.assertEqual(newlist.search(1).value, 1)
        self.assertEqual(newlist.search(-1), None)

linkListMethodsSuite = unittest.TestLoader(
).loadTestsFromTestCase(TestLinkListMethods)
unittest.TextTestRunner(verbosity=2).run(linkListMethodsSuite)
