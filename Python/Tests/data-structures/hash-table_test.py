#!/usr/bin/python3
import unittest
import sys
import os
mod_directory = [os.getcwd() + '/Data Structures']
mod_directory.extend(sys.path)
sys.path = mod_directory
from hashtable import HashTableOA, HashTableChain


class TestHashTables(unittest.TestCase):

    def test_open_addressing(self):
        for i in range(100):
            ht = HashTableOA()
            ht.insert('a', 1)
            ht.insert('b', 2)
            ht.insert('c', 3)
            ht.insert('d', 4)
            ht.insert('e', 5)
            ht.insert('f', 6)
            ht.insert('g', 7)
            ht.insert('h', 8)
            ht.insert('i', 9)
            ht.insert('j', 10)
            ht.insert('k', 11)
            self.assertEqual(ht.search('a'), 1)
            self.assertEqual(ht.search('k'), 11)
            self.assertEqual(ht.search('g'), 7)
            self.assertEqual(ht.search('d'), 4)
            self.assertEqual(ht.search('f'), 6)
            self.assertEqual(ht.size, 11)
            ht.delete('d')
            ht.delete('g')
            self.assertEqual(ht.search('d'), None)
            self.assertEqual(ht.search('g'), None)
            self.assertEqual(ht.size, 9)
            self.assertEqual(ht.m, 16)
            ht.insert('g', 101)
            self.assertEqual(ht.search('g'), 101)
            ht.delete('a')
            ht.delete('b')
            ht.delete('c')
            ht.delete('h')
            ht.delete('e')
            ht.delete('f')
            ht.delete('g')
            self.assertEqual(ht.size, 3)
            self.assertEqual(ht.m, 8)

    def test_chaining(self):
        for i in range(100):
            ht = HashTableChain()
            ht.insert('a', 1)
            ht.insert('b', 2)
            ht.insert('c', 3)
            ht.insert('d', 4)
            ht.insert('e', 5)
            ht.insert('f', 6)
            ht.insert('g', 7)
            ht.insert('h', 8)
            ht.insert('i', 9)
            ht.insert('j', 10)
            ht.insert('k', 11)
            self.assertEqual(ht.search('a'), 1)
            self.assertEqual(ht.search('k'), 11)
            self.assertEqual(ht.search('g'), 7)
            self.assertEqual(ht.search('d'), 4)
            self.assertEqual(ht.search('f'), 6)
            self.assertEqual(ht.size, 11)
            ht.delete('d')
            ht.delete('g')
            self.assertEqual(ht.search('d'), None)
            self.assertEqual(ht.search('g'), None)
            self.assertEqual(ht.size, 9)
            ht.insert('g', 101)
            self.assertEqual(ht.search('g'), 101)
            ht.delete('a')
            ht.delete('b')
            ht.delete('c')
            ht.delete('h')
            ht.delete('e')
            ht.delete('f')
            ht.delete('g')
            self.assertEqual(ht.size, 3)
            self.assertEqual(ht.m, 8)

def main():
    hashTableSuite = unittest.TestLoader().loadTestsFromTestCase(TestHashTables)
    unittest.TextTestRunner(verbosity=2).run(hashTableSuite)
