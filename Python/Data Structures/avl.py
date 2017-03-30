from bst import BSTNode, BST

class AVLNode(BSTNode):

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def isRH(self):
        if self.left is not None:
            leftHeight = self.left.height
        else:
            leftHeight = -1
        if self.right is not None:
            rightHeight = self.right.height
        else:
            rightHeight = -1
        if leftHeight < rightHeight:
            return True
        else:
            return False

    def isLH(self):
        if self.left is not None:
            leftHeight = self.left.height
        else:
            leftHeight = -1
        if self.right is not None:
            rightHeight = self.right.height
        else:
            rightHeight = -1
        if leftHeight > rightHeight:
            return True
        else:
            return False

    def setHeight(self):
        if self.left is not None:
            lHeight = self.left.height
        else:
            lHeight = -1
        if self.right is not None:
            rHeight = self.right.height
        else:
            rHeight = -1
        self.height = max(lHeight, rHeight) + 1
        # print('Set height of node', self.key, self.height)
        if self.parent is not None:
            self.parent.setHeight()

    def balanced(self):
        if self.left is not None:
            leftHeight = self.left.height
        else:
            leftHeight = -1
        if self.right is not None:
            rightHeight = self.right.height
        else:
            rightHeight = -1
        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True


class AVL(BST):

    def insert(self, key, data):
        self.size += 1
        if self.root is None:
            self.root = AVLNode(key, data)
        else:
            thisNode = self.root
            while thisNode is not None:
                if thisNode.key < key:
                    if thisNode.right is None:
                        thisNode.right = AVLNode(key, data)
                        thisNode.right.parent = thisNode
                        thisNode.setHeight()
                        self.fix_avl(thisNode)
                        thisNode = None
                    else:
                        thisNode = thisNode.right
                elif thisNode.key > key:
                    if thisNode.left is None:
                        thisNode.left = AVLNode(key, data)
                        thisNode.left.parent = thisNode
                        thisNode.setHeight()
                        self.fix_avl(thisNode)
                        thisNode = None
                    else:
                        thisNode = thisNode.left
                else:
                    # Duplicate key, skip insertion
                    thisNode = None

    def fix_avl(self, node):
        parent = node.parent
        if node.isRH() and not node.balanced():
            if node.right is not None and node.right.isLH():
                self.rRotate(node.right)
                self.lRotate(node)
            else:
                self.lRotate(node)
        elif node.isLH() and not node.balanced():
            if node.left is not None and node.left.isRH():
                self.lRotate(node.left)
                self.rRotate(node)
            else:
                self.rRotate(node)
        if parent is not None:
            self.fix_avl(parent)
            return

    def rRotate(self, node):
        L = node.left
        R = L.right
        P = node.parent
        if P is None:
            if R is None:
                L.right = node
                node.left = None
                node.parent = L
                self.root = L
                L.parent = None
            else:
                node.left = R
                R.parent = node
                L.right = node
                node.parent = L
                self.root = L
                L.parent = None
        elif P.right is node:
            if R is None:
                L.right = node
                node.left = None
                node.parent = L
                L.parent = P
                P.right = L
            else:
                node.left = R
                R.parent = node
                L.right = node
                node.parent = L
                L.parent = P
                P.right = L
        elif P.left is node:
            if R is None:
                L.right = node
                node.left = None
                node.parent = L
                L.parent = P
                P.left = L
            else:
                node.right = R
                R.parent = node
                L.right = node
                node.parent = L
                L.parent = P
                P.left = L
        node.setHeight()

    def lRotate(self, node):
        R = node.right
        L = R.left
        P = node.parent
        if P is None:
            if L is None:
                R.left = node
                node.right = None
                node.parent = R
                R.parent = None
                self.root = R
            else:
                node.right = L
                L.parent = node
                node.right = L
                R.left = node
                node.parent = R
                R.parent = None
                self.root = R
        elif P.left is node:
            if L is None:
                R.left = node
                node.right = None
                node.parent = R
                R.parent = P
                P.left = R
            else:
                node.right = L
                L.parent = node
                R.left = node
                node.parent = R
                R.parent = P
                P.left = R
        elif P.right is node:
            if L is None:
                R.left = node
                node.right = None
                node.parent = R
                R.parent = P
                P.right = R
            else:
                node.right = L
                L.parent = node
                R.left = node
                node.parent = R
                R.parent = P
                P.right = R
        node.setHeight()
