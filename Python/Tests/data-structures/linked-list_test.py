#!/usr/bin/python3
import unittest
import sys
import os
from random import randint
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from linkedlist import LinkList, Node


class TestLinkListMethods(unittest.TestCase):

    def test_init(self):
        # Should return an object with a single property:
        # self.head == None
        newList = LinkList()
        self.assertIsInstance(newList, LinkList)
        self.assertEqual(newList.head, None)

    def test_insert(self):
        # Should insert new values at the START of the list via pointer
        # manipulation.
        new_list = LinkList()

        for i in range(100):
            r = randint(0, 100)
            new_list.insert(r)
            self.assertIsInstance(new_list.head, Node)
            self.assertEqual(new_list.head.value, r)
            if i > 1:
                self.assertIsInstance(new_list.head.next, Node)


    def test_remove(self):
        new_list = LinkList()

        new_list.insert(1)
        new_list.insert(2)
        self.assertEqual(new_list.head.value, 2)
        self.assertEqual(new_list.remove().value, 2)
        self.assertEqual(new_list.head.value, 1)
        self.assertEqual(new_list.remove().value, 1)
        self.assertEqual(new_list.head, None)
        self.assertEqual(new_list.remove(), None)

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

def main():
    linkListMethodsSuite = unittest.TestLoader().loadTestsFromTestCase(TestLinkListMethods)
    unittest.TextTestRunner(verbosity=2).run(linkListMethodsSuite)
