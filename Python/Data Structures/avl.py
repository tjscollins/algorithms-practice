from bst import BSTNode, BST


class AVLNode(BSTNode):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def _is_rh(self):
        left, right = self._get_children_heights()
        return right > left

    def _is_lh(self):
        left, right = self._get_children_heights()
        return right < left

    def _is_bal(self):
        (left, right) = self._get_children_heights()
        return abs(left - right) <= 1

    def _set_height(self):
        self.height = max(self._get_children_heights()) + 1

    def _get_children_heights(self):
        if self.left is None:
            left = -1
        else:
            left = self.left.height
        if self.right is None:
            right = -1
        else:
            right = self.right.height
        return (left, right)


class AVL(BST):
    # Inherits:
    # def __init__(self):
    #     self.root = None
    #     self.size = 0

    def insert(self, key, data):
        if self.root is None:
            self.root = AVLNode(key, data)
            self.size = 1
        else:
            node = self.root
            while node is not None:
                if key < node.key:
                    if node.left is None:
                        node.left = AVLNode(key, data)
                        node.left.parent = node
                        self.size += 1
                        node._set_height()
                        self.fix_avl(node.parent)
                        node = None
                    else:
                        node = node.left
                elif key > node.key:
                    if node.right is None:
                        node.right = AVLNode(key, data)
                        node.right.parent = node
                        self.size += 1
                        node._set_height()
                        self.fix_avl(node.parent)
                        node = None
                    else:
                        node = node.right
                else:
                    # Ignore dupliate keys
                    node = None

    def delete(self, key):
        node = self.search(key)
        while node is not None:
            if node.left is None or node.right is None:
                if node is node.parent.left:
                    node.parent.left = node.left or node.right
                    if node.parent.left is not None:
                        node.parent.left.parent = node.parent
                else:
                    node.parent.right = node.left or node.right
                    if node.parent.right is not None:
                        node.parent.right.parent = node.parent
                self.fix_avl(node.parent)
                return node
            else:
                n = self.__next__(node)
                node.key, n.key = n.key, node.key
                node.data, n.data = n.data, node.data
                node = n


    def fix_avl(self, node):
        while node is not None:
            node._set_height()
            if not node._is_bal():
                if node._is_lh():
                    if node.left._is_lh():
                        self._right_rotate(node)
                    else:
                        self._left_rotate(node.left)
                        self._right_rotate(node)
                elif node._is_rh():
                    if node.right._is_rh():
                        self._left_rotate(node)
                    else:
                        self._right_rotate(node.right)
                        self._left_rotate(node)
            node = node.parent


    def _right_rotate(self, node):
        x = node
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            else:
                y.parent.right = y

        x.left = y.right
        if x.left is not None:
            x.left.parent = x

        y.right = x
        x.parent = y

        x._set_height()
        y._set_height()

    def _left_rotate(self, node):
        x = node
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            else:
                y.parent.right = y

        x.right = y.left
        if x.right is not None:
            x.right.parent = x

        y.left = x
        x.parent = y

        x._set_height()
        y._set_height()

def count_bst_nodes(root):
    return 0 if root is None else 1 + count_bst_nodes(root.left) + count_bst_nodes(root.right)
