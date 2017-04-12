from bst import BSTNode, BST


class AVLNode(BSTNode):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.left_height = -1
        self.right_height = -1

    def isRH(self):
        return self.right_height > self.left_height

    def isLH(self):
        return self.right_height < self.left_height

    def isBal(self):
        return self.left_height == self.right_height

    def setHeight(self):
        if self.left is None:
            self.left_height = -1
        else:
            self.left_height = self.left.height
        if self.right is None:
            self.right_height = -1
        else:
            self.right_height = self.right.height

        self.height = max(self.left_height, self.right_height) + 1



class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        if self.root is None:
            self.root = AVLNode(key, data)
            self.size = 1
        else:
            node = self.root
            while node is not None:
                if key < node.key:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = AVLNode(key, data)
                        node.left.parent = node
                        node.setHeight()
                        self.size += 1
                        if node.parent is not None and node.parent.parent is not None:
                            self.fix_avl(node.parent.parent)
                        node = None
                elif key > node.key:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = AVLNode(key, data)
                        node.right.parent = node
                        node.setHeight()
                        self.size += 1
                        if node.parent is not None and node.parent.parent is not None:
                            self.fix_avl(node.parent.parent)
                        node = None



    def search(self, key):
        pass

    def traverse_inorder(self):
        pass

    def delete(self, key):
        pass

    def fix_avl(self, node):
        return

    def rRotate(self, node):
        pass

    def lRotate(self, node):
        pass
