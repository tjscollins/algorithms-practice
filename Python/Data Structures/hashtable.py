import random
import math


class HashTableChain:

    def __init__(self):
        self.m = int(2**3)
        self.table = [[None, None, None]] * self.m
        self.size = 0
        self.a = random.random() * (2**32 - 1)

    def hashOne(self, key):
        # Multiplication Method
        return (int((self.a * hash(key)) % 2**32) >> int(32 - math.log(self.m, 2))) % self.m

    def insert(self, key, data):
        h = self.hashOne(key)
        entry = self.table[h]
        while entry[2] is not None:
            entry = entry[2]
        entry[2] = [key, data, None]
        self.size += 1

    def search(self, key):
        h = self.hashOne(key)
        entry = self.table[h]
        while entry[0] is not key and entry[2] is not None:
            entry = entry[2]
        if entry[0] is key:
            return entry[1]
        else:
            return None

    def delete(self, key):
        h = self.hashOne(key)
        entry = self.table[h]
        parent = None
        while entry[0] is not key and entry[2] is not None:
            parent = entry
            entry = entry[2]
        if entry[0] is key:
            self.size -= 1
            if parent is None:
                self.table[h] = entry[2]
            else:
                parent[2] = entry[2]
            return entry
        else:
            return None


class HashTableOA:

    def __init__(self):
        self.m = int(2**3)
        self.size = 0
        self.table = [None] * self.m
        self.a = random.random() * (2**32 - 1)
        self.b = random.random() * (2**32 - 1)

    def hashOne(self, key):
        # Multiplication Method
        return (int((hash(key) * self.a % 2**32)) >> int(32 - math.log(self.m, 2))) % self.m

    def hashTwo(self, key):
        # Multiplication Method -- Always Odd
        h = (int((hash(key) * self.b % 2**32)) >>
             int(32 - math.log(self.m, 2))) % self.m
        if h % 2 == 0:
            h += 1
        return h

    def insert(self, key, data):
        if self.size is self.m:
            self.double(key, data)
            return
        for i in range(self.m):
            h = (self.hashOne(key) + i * self.hashTwo(key)) % self.m
            if self.table[h] is None or self.table[h] is 'DELETED':
                self.size += 1
                self.table[h] = [key, data]
                return

    def double(self, key, data):
        array = self.table
        self.m *= 2
        self.table = [None] * self.m
        self.size = 0
        for a in array:
            self.insert(a[0], a[1])
        self.insert(key, data)

    def halve(self):
        array = self.table
        self.m //= 2
        self.table = [None] * self.m
        self.size = 0
        for a in array:
            if a is not None and a is not 'DELETED':
                self.insert(a[0], a[1])

    def search(self, key):
        for i in range(self.m):
            h = (self.hashOne(key) + i * self.hashTwo(key)) % self.m
            if self.table[h] is None:
                return None
            elif self.table[h] is not 'DELETED' and self.table[h][0] is key:
                return self.table[h][1]
        return None

    def delete(self, key):
        if self.size <= self.m // 4:
            self.halve()
        for i in range(self.m):
            h = (self.hashOne(key) + i * self.hashTwo(key)) % self.m
            if self.table[h] is None:
                return None
            elif self.table[h] is not 'DELETED' and self.table[h][0] is key:
                self.size -= 1
                self.table[h] = 'DELETED'
