#!/usr/bin/python

import unittest
execfile('../../Data Structures/linked-list.py')
execfile('../../Data Structures/bst.py')
execfile('../../Data Structures/avl.py')
execfile('../../Data Structures/heap.py')
execfile('../../Data Structures/hash-table.py')


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


class TestAVLMethods(unittest.TestCase):

    def test_insert(self):
        newbst = AVL()
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

    def test_traverse_inorder(self):
        newbst = AVL()
        newbst.insert(5, 5)
        newbst.insert(2, 3)
        newbst.insert(7, 16)
        newbst.insert(8, 16)
        newbst.insert(1, 100)
        newbst.insert(4, -4)
        newbst.insert(6, 2)
        self.assertListEqual(newbst.traverse_inorder(), [[1, 100], [2, 3], [
                             4, -4], [5, 5], [6, 2], [7, 16], [8, 16]])

    def test_rotate(self):
        newavl = AVL()
        newavl.insert(2, 2)
        newavl.insert(1, 1)
        newavl.insert(3, 3)
        newavl.root.rRotate()
        print([newavl.root.key, newavl.root.left, newavl.root.right])
        self.assertTrue(newavl.root.key == 3)

    def test_height(self):
        newbst = AVL()
        newbst.insert(1, 100)
        newbst.insert(2, 3)
        newbst.insert(4, -4)
        newbst.insert(5, 5)
        newbst.insert(6, 2)
        newbst.insert(7, 16)
        newbst.insert(8, 16)
        newbst.insert(9, 16)
        newbst.insert(10, 16)
        self.assertTrue(newbst.root.balanced())
        # self.assertLessEqual(newbst.root.height, 6)


class TestHeapMethods(unittest.TestCase):

    def test_build_heaps(self):
        newHeap = Heap([3, 2, 1, 5, 6, 4], 'max')
        self.assertListEqual(newHeap.array, [6, 5, 4, 3, 2, 1])
        newHeap = Heap([3, 2, 1, 5, 6, 4], 'min')
        self.assertListEqual(newHeap.array, [1, 2, 3, 5, 6, 4])

    def test_heap_sort(self):
        newHeap = Heap([1, 2, -1, 5, 10, 13, -3, 25, 12], 'max')
        self.assertListEqual(newHeap.heapSort(),
                             [-3, -1, 1, 2, 5, 10, 12, 13, 25])
        newHeap = Heap([1, 2, -1, 5, 10, 13, -3, 25, 12], 'min')
        self.assertListEqual(newHeap.heapSort(), [
                             25, 13, 12, 10, 5, 2, 1, -1, -3])


class TestHashTables(unittest.TestCase):

    def test_open_addressing(self):
        ht = HashTableOA()
        ht.insert('a', 1)
        ht.insert('b', 2)
        ht.insert('c', 3)
        ht.insert('d', 4)
        # self.assertEqual(ht.search('a'), 1)
        # self.assertEqual(ht.search('b'), 2)
        # self.assertEqual(ht.search('c'), 3)
        # self.assertEqual(ht.search('d'), 4)


linkListSuite = unittest.TestLoader().loadTestsFromTestCase(TestLinkListMethods)
bstSuite = unittest.TestLoader().loadTestsFromTestCase(TestBSTMethods)
avlSuite = unittest.TestLoader().loadTestsFromTestCase(TestAVLMethods)
heapSuite = unittest.TestLoader().loadTestsFromTestCase(TestHeapMethods)
hashTableSuite = unittest.TestLoader().loadTestsFromTestCase(TestHashTables)

dataStructureSuite = unittest.TestSuite(
    [linkListSuite, bstSuite, avlSuite, heapSuite, hashTableSuite])
unittest.TextTestRunner(verbosity=2).run(dataStructureSuite)
