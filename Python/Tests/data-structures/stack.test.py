#!/usr/bin/python

import unittest
execfile('./Data Structures/stack.py')

class TestStackMethods(unittest.TestCase):
    def test_push(self):
        newStack = Stack()
        newStack.push(1)
        newStack.push(2)
        newStack.push(3)
        newStack.push(4)
        self.assertEqual(newStack.count, 4)
        self.assertListEqual(newStack.stack, [1, 2, 3, 4])

    def test_pop(self):
        newStack = Stack()
        newStack.push(1)
        newStack.push(2)
        self.assertEqual(newStack.count, 2)
        self.assertEqual(newStack.pop(), 2)
        self.assertEqual(newStack.count, 1)

    def test_last(self):
        newStack = Stack()
        self.assertEqual(newStack.last(), None)
        newStack.push(1)
        newStack.push(2)
        self.assertEqual(newStack.last(), 2)

    def test_list(self):
        newStack = Stack()
        newStack.push(1)
        newStack.push(2)
        newStack.push(3)
        newStack.push(4)
        newStack.push(5)
        self.assertEqual(newStack.list(), [5, 4, 3, 2, 1])

stackMethodSuite = unittest.TestLoader().loadTestsFromTestCase(TestStackMethods)
unittest.TextTestRunner(verbosity=2).run(stackMethodSuite)
