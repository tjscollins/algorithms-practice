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
        self.size += 1
        if self.root is None:
            self.root = BSTNode(key, data)
        else:
            thisNode = self.root
            while thisNode is not None:
                if thisNode.key < key:
                    if thisNode.right is None:
                        thisNode.right = BSTNode(key, data)
                        thisNode.right.parent = thisNode
                        thisNode = None
                    else:
                        thisNode = thisNode.right
                elif thisNode.key > key:
                    if thisNode.left is None:
                        thisNode.left = BSTNode(key, data)
                        thisNode.left.parent = thisNode
                        thisNode = None
                    else:
                        thisNode = thisNode.left
                else:
                    # Duplicate key, skip insertion
                    thisNode = None

    def search(self, key):
        thisNode = self.root
        while thisNode is not None:
            # print(thisNode.key, key, thisNode.right, thisNode.left)
            if thisNode.key == key:
                return thisNode
            elif thisNode.key < key:
                thisNode = thisNode.right
            elif thisNode.key > key:
                thisNode = thisNode.left
        return None

    def traverse_inorder(self):
        output = [[None]]
        thisNode = self.root
        while (len(output) < self.size + 1):
            if thisNode.left is not None and [thisNode.left.key, thisNode.left.data] not in output:
                thisNode = thisNode.left
            else:
                if [thisNode.key, thisNode.data] not in output:
                    output.append([thisNode.key, thisNode.data])
                if thisNode.right is not None and [thisNode.right.key, thisNode.right.data] not in output:
                    thisNode = thisNode.right
                else:
                    thisNode = thisNode.parent

        return output[1:]

    # def delete(self, key):
    #     thisNode = self.root
    #     while thisNode is not None:
    #         if thisNode.key == key:
    #
    #         elif thisNode.key < key:
    #             thisNode = thisNode.right
    #         elif thisNode.key > key:
    #             thisNode = thisNode.left
    #     return None
