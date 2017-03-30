#!/usr/bin/python

class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self, item):
        self.stack.append(item)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.stack.pop()

    def last(self):
        if self.count is 0:
            return None
        else:
            return self.stack[-1]

    def list(self):
        # Returns 'stack' order, i.e. LIFO
        return self.stack[::-1]
