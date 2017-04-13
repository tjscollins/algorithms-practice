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
        return abs(self.left_height - self.right_height) <= 1

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
        if self.parent is not None:
            self.parent.setHeight()



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
                        self.fix_avl(node)
                        node = None
                elif key > node.key:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = AVLNode(key, data)
                        node.right.parent = node
                        node.setHeight()
                        self.size += 1
                        self.fix_avl(node)
                        node = None
        # print('Node count: ', count_bst_nodes(self.root), self.size);


    # def search(self, key):
    #     pass

    # def traverse_inorder(self):
    #     pass

    def delete(self, key):
        pass

    def fix_avl(self, node):
        if node is None:
            return
        elif node.isBal():
            self.fix_avl(node.parent)
            return

        parent = node.parent
        if node.isRH():
            if node.right.isLH():
                self.__right_rotate__(node.right)
                self.__left_rotate__(node)
            else:
                self.__left_rotate__(node)
        else:
            if node.left.isRH():
                self.__left_rotate__(node.left)
                self.__right_rotate__(node)
            else:
                self.__right_rotate__(node)

        if parent is not None:
            self.fix_avl(parent)

    def __right_rotate__(self, node):
        x = node
        y = node.left

        b = y.right

        y.right = x
        if x.parent is None:
            y.parent = None
            self.root = y
        else:
            y.parent = x.parent
            if x is x.parent.right:
                y.parent.right = y
            else:
                y.parent.left = y
        x.parent = y

        x.left = b
        if b is not None:
            b.parent = x

        x.setHeight()
        y.setHeight()

    def __left_rotate__(self, node):
        x = node
        y = node.right

        b = y.left

        y.left = x
        if x.parent is None:
            y.parent = None
            self.root = y
        else:
            y.parent = x.parent
            if x is x.parent.right:
                y.parent.right = y
            else:
                y.parent.left = y
        x.parent = y

        x.right = b
        if b is not None:
            b.parent = x

        x.setHeight()
        y.setHeight()

def count_bst_nodes(root):
    return 0 if root is None else 1 + count_bst_nodes(root.left) + count_bst_nodes(root.right)
