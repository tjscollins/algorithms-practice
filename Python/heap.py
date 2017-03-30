import math


class Heap:

    def __init__(self, array, direction):
        self.array = array
        self.size = len(array)
        self.type = direction
        if direction is 'max':
            self.makeMaxHeap()
        elif direction is 'min':
            self.makeMinHeap()
        # else:
            # Error

    def makeMaxHeap(self):
        for i in range(int(math.floor(math.log(self.size, 2))), -1, -1):
            self.maxHeapify(i)

    def maxHeapify(self, i):
        large = i
        if self.size >= 2 * i + 2 and self.array[large] < self.array[2 * i + 1]:
            large = 2 * i + 1
        if self.size >= 2 * i + 3 and self.array[large] < self.array[2 * i + 2]:
            large = 2 * i + 2
        if large != i:
            self.array[large], self.array[i] = self.array[i], self.array[large]
            self.maxHeapify(large)

    def makeMinHeap(self):
        for i in range(int(math.floor(math.log(self.size, 2))), -1, -1):
            self.minHeapify(i)

    def minHeapify(self, i):
        small = i
        if self.size >= 2 * i + 2 and self.array[small] > self.array[2 * i + 1]:
            small = 2 * i + 1
        if self.size >= 2 * i + 3 and self.array[small] > self.array[2 * i + 2]:
            small = 2 * i + 2
        if small != i:
            self.array[small], self.array[i] = self.array[i], self.array[small]
            self.minHeapify(small)

    def heapSort(self):
        while self.size > 0:
            self.array[0], self.array[self.size -
                                      1] = self.array[self.size - 1], self.array[0]
            self.size -= 1
            if self.type is 'max':
                self.maxHeapify(0)
            elif self.type is 'min':
                self.minHeapify(0)

        return self.array
