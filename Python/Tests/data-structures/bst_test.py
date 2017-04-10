#!/usr/bin/python3
import unittest
import sys
import os
import math
from random import randint
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from bst import BST


class TestBSTMethods(unittest.TestCase):

    def test_insert(self):
        newbst = BST()
        newbst.insert(5000, 5)
        newbst.insert(2000, 3)
        newbst.insert(6000, 16)
        for i in range(1000):
            newbst.insert(randint(1, 10000), 10)

        self.assertEqual(count_bst_nodes(newbst.root), newbst.size)
        self.assertTrue(has_bst_property(newbst.root))
        self.assertEqual(newbst.root.key, 5000)
        self.assertEqual(newbst.root.data, 5)
        self.assertEqual(newbst.root.left.key, 2000)
        self.assertEqual(newbst.root.left.data, 3)
        self.assertEqual(newbst.root.right.key, 6000)
        self.assertEqual(newbst.root.right.data, 16)

    def test_search(self):
        for j in range(100):
            newbst = BST()
            for i in range(100):
                key = randint(1, 1000)
                if key != 500 and key != 600 and key != 400:
                    newbst.insert(key, key)
            newbst.insert(400, 500)
            newbst.insert(500, 50)
            newbst.insert(600, 5)
            self.assertEqual(newbst.search(400).data, 500)
            self.assertEqual(newbst.search(500).data, 50)
            self.assertEqual(newbst.search(600).data, 5)

    def test_traverse_inorder(self):
        for j in range(100):
            newbst = BST()
            array = []
            for i in range(100):
                key = randint(1, 100)
                array.append(key)
                newbst.insert(key, key)
            # Remove duplicate entries because duplicate keys are ignored
            arr = sorted(list(set(array)))
            self.assertListEqual(newbst.traverse_inorder(), arr)

    def test_delete(self):
        for j in range(100):
            newbst = BST()
            target = randint(1,1000)
            for i in range(100):
                key = randint(1, 1000)
                if key != target:
                    newbst.insert(key, key)
            newbst.insert(target, 1)
            self.assertEqual(newbst.search(target).data, 1)
            newbst.delete(target)
            self.assertEqual(newbst.search(target), None)


def main():
    bstMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestBSTMethods)
    unittest.TextTestRunner(verbosity=3).run(bstMethodSuite)


def has_bst_property(node):
    if node is None:
        return True
    left = node.left.key < node.key if node.left is not None else True
    right = node.right.key >= node.key if node.right is not None else True
    return left and right and has_bst_property(node.left) and has_bst_property(node.right)


def count_bst_nodes(root):
    return 0 if root is None else 1 + count_bst_nodes(root.left) + count_bst_nodes(root.right)
