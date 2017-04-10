class BSTNode:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        if self.root is None:
            self.root = BSTNode(key, data)
            self.size += 1
        else:
            node = self.root
            while node is not None:
                if key < node.key:
                    if node.left is None:
                        node.left = BSTNode(key, data)
                        self.size += 1
                        node.left.parent = node
                        node = None
                    else:
                        node = node.left
                elif key > node.key:
                    if node.right is None:
                        node.right = BSTNode(key, data)
                        self.size += 1
                        node.right.parent = node
                        node = None
                    else:
                        node = node.right
                else:
                    # Ignore duplicate keys
                    node = None


    def search(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                break
        return node

    def traverse_inorder(self):
        out = []
        node = self.root
        while node.left is not None:
            node = node.left
        while node is not None:
            out.append(node.key)
            # print(out)
            node = self.__next__(node)
        return out

    def delete(self, key):
        node = self.search(key)
        if node is not None:
            if node.left is None or node.right is None:
                if node is node.parent.left:
                    node.parent.left = node.left or node.right
                    if node.parent.left is not None:
                        node.parent.left.parent = node.parent
                else:
                    node.parent.right = node.left or node.right
                    if node.parent.right is not None:
                        node.parent.right.parent = node.parent
                return node
            else:
                n = self.__next__(node)
                node.key, n.key = n.key, node.key
                node.data, n.data = n.data, node.data
                return self.delete(node.key)

    def __next__(self, node):
        if node.right is not None:
            current = node.right
            while current.left is not None:
                current = current.left
            return current
        else:
            current = node
            while current.parent is not None and current is current.parent.right:
                current = current.parent
            return current.parent
