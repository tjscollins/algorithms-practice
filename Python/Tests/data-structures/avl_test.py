#!/usr/bin/python3
import unittest
import math
import random
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from avl import AVL


class TestAVLMethods(unittest.TestCase):

    def test_insert(self):
        newAVL = AVL()
        newAVL.insert(5, 5)
        newAVL.insert(3, 1)
        newAVL.insert(8, 16)
        self.assertEqual(newAVL.root.key, 5)
        self.assertEqual(newAVL.root.left.key, 3)
        self.assertEqual(newAVL.root.right.key, 8)

    def test_random_inserts(self):
        newbst = AVL()
        for i in range(20):
            newbst.insert(int(random.random() * 1000), i)
        self.assertLess(newbst.root.height,  2 *
                        math.log(newbst.size + 1, 2))

    def test_sorted_inserts(self):
        newbst = AVL()
        for i in range(100):
            newbst.insert(i, i)
        self.assertLess(newbst.root.height,  1.45 *
                        math.log(newbst.size + 1, 2))

    def test_search(self):
        newbst = AVL()
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
    #
    # def test_traverse_inorder(self):
    #     newbst = AVL()
    #     newbst.insert(5, 5)
    #     newbst.insert(2, 3)
    #     newbst.insert(7, 16)
    #     newbst.insert(8, 16)
    #     newbst.insert(1, 100)
    #     newbst.insert(4, -4)
    #     newbst.insert(6, 2)
    #     self.assertListEqual(newbst.traverse_inorder(), [[1,100], [2,3], [4,-4], [5,5], [6,2], [7,16], [8,16]])
    #
    # def test_rotate(self):
    #     newavl = AVL()
    #     newavl.insert(2, 2)
    #     newavl.insert(1, 1)
    #     newavl.insert(3, 3)
    #     newavl.root.rRotate()
    #     print([newavl.root.key, newavl.root.left, newavl.root.right])
    #     self.assertTrue(newavl.root.key == 3)
    #
    # def test_height(self):
    #     newbst = AVL()
    #     newbst.insert(1, 100)
    #     newbst.insert(2, 3)
    #     newbst.insert(4, -4)
    #     newbst.insert(5, 5)
    #     newbst.insert(6, 2)
    #     newbst.insert(7, 16)
    #     newbst.insert(8, 16)
    #     newbst.insert(9, 16)
    #     newbst.insert(10, 16)
    #     self.assertTrue(newbst.root.balanced())
        # self.assertLessEqual(newbst.root.height, 6)


def main():
    avlMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestAVLMethods)
    unittest.TextTestRunner(verbosity=2).run(avlMethodSuite)
