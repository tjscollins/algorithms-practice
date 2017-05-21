class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def remove(self):
        if self.head is not None:
            node = self.head
            self.head = node.next
            return node
        else:
            return None

    def traverse(self):
        out = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

    def search(self, data):
        node = self.head
        while node is not None:
            if node.value == data:
                return node
            else:
                node = node.next
        return None
