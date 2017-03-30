#!/usr/bin/python3
import unittest
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from bst import BST


class TestBSTMethods(unittest.TestCase):

    def test_insert(self):
        newbst = BST()
        newbst.insert(5, 5)
        newbst.insert(2, 3)
        newbst.insert(6, 16)
        self.assertEqual(newbst.root.key, 5)
        self.assertEqual(newbst.root.data, 5)
        self.assertEqual(newbst.root.left.key, 2)
        self.assertEqual(newbst.root.left.data, 3)
        self.assertEqual(newbst.root.right.key, 6)
        self.assertEqual(newbst.root.right.data, 16)

    def test_search(self):
        newbst = BST()
        newbst.insert(5, 5)
        newbst.insert(3, 1)
        newbst.insert(8, 16)
        newbst.insert(1, 100)
        newbst.insert(4, -4)
        newbst.insert(6, 0)
        newbst.insert(10, 10)
        self.assertEqual(newbst.search(6).data, 0)
        self.assertEqual(newbst.search(15), None)
        self.assertEqual(newbst.search(25), None)
        self.assertEqual(newbst.search(10).data, 10)
        self.assertEqual(newbst.search(1).data, 100)

    def test_traverse_inorder(self):
        newbst = BST()
        newbst.insert(5, 5)
        newbst.insert(2, 3)
        newbst.insert(7, 16)
        newbst.insert(8, 16)
        newbst.insert(1, 100)
        newbst.insert(4, -4)
        newbst.insert(6, 2)
        self.assertListEqual(newbst.traverse_inorder(), [[1, 100], [2, 3], [
                             4, -4], [5, 5], [6, 2], [7, 16], [8, 16]])


bstMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestBSTMethods)
unittest.TextTestRunner(verbosity=2).run(bstMethodSuite)
