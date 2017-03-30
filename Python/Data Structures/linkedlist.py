class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) Time Complexity
    def insert(self, data):
        self.size += 1
        thisNode = self.head
        self.head = Node(data)
        if thisNode is not None:
            self.head.next = thisNode

    # O(1) Time Complexity
    def remove(self):
        self.size -= 1
        self.head = self.head.next

    # O(n) Time complexity
    def traverse(self):
        output = []
        thisNode = self.head
        while thisNode is not None:
            # print str(thisNode.value)
            output.append(thisNode.value)
            thisNode = thisNode.next
        return output

    # O(n) Time Complexity
    def search(self, data):
        thisNode = self.head
        while thisNode is not None:
            if thisNode.value == data:
                return thisNode
            else:
                thisNode = thisNode.next
        return None
