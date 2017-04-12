#!/usr/bin/python3
import unittest
import math
from random import randint
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from avl import AVL


class TestAVLMethods(unittest.TestCase):

    def test_insert(self):
        newbst = AVL()
        newbst.insert(5000, 5)
        newbst.insert(2000, 3)
        newbst.insert(6000, 16)
        for i in range(1000):
            newbst.insert(randint(1, 10000), 10)

        self.assertEqual(count_bst_nodes(newbst.root), newbst.size)
        self.assertTrue(newbst.root is not None)
        self.assertTrue(has_avl_property(newbst.root))

    # def test_search(self):
    #     for j in range(100):
    #         newbst = AVL()
    #         for i in range(100):
    #             key = randint(1, 1000)
    #             if key != 500 and key != 600 and key != 400:
    #                 newbst.insert(key, key)
    #         newbst.insert(400, 500)
    #         newbst.insert(500, 50)
    #         newbst.insert(600, 5)
    #         self.assertEqual(newbst.search(400).data, 500)
    #         self.assertEqual(newbst.search(500).data, 50)
    #         self.assertEqual(newbst.search(600).data, 5)

    # def test_traverse_inorder(self):
    #     for j in range(100):
    #         newbst = AVL()
    #         array = []
    #         for i in range(100):
    #             key = randint(1, 100)
    #             array.append(key)
    #             newbst.insert(key, key)
    #         # Remove duplicate entries because duplicate keys are ignored
    #         arr = sorted(list(set(array)))
    #         self.assertListEqual(newbst.traverse_inorder(), arr)
    #
    # def test_delete(self):
    #     for j in range(100):
    #         newbst = AVL()
    #         target = randint(1,1000)
    #         for i in range(100):
    #             key = randint(1, 1000)
    #             if key != target:
    #                 newbst.insert(key, key)
    #         newbst.insert(target, 1)
    #         self.assertEqual(newbst.search(target).data, 1)
    #         newbst.delete(target)
    #         self.assertEqual(newbst.search(target), None)


def main():
    avlMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestAVLMethods)
    unittest.TextTestRunner(verbosity=2).run(avlMethodSuite)

def has_avl_property(node):
    if node is None:
        return True
    if node.left is not None:
        left = node.left.key < node.key
        hLeft = node.left.height
    else:
        left = True
        hLeft = -1
    if node.right is not None:
        right = node.right.key < node.key
        hRight = node.right.height
    else:
        right = True
        hRight = -1

    bal = abs(hLeft - hRight) <= 1 and node.height == max(hLeft, hRight) + 1

    return bal and left and right and has_avl_property(node.left) and has_avl_property(node.right)


def count_bst_nodes(root):
    return 0 if root is None else 1 + count_bst_nodes(root.left) + count_bst_nodes(root.right)
