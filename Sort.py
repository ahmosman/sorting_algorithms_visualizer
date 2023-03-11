import time, sys

from helpers import sedgewick, shell, heapify, quick

sys.setrecursionlimit(99999999)
class Sort:
    def insertionSort(self, data):
        start = time.time()
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        end = time.time()
        return end - start

    def selectionSort(self, data):
        start = time.time()
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        end = time.time()
        return end - start

    def shellSortSedgwick(self, data):
        start = time.time()
        sedgewick_reversed = sedgewick(len(data))[::-1]
        for k in sedgewick_reversed:
            data = shell(data, k)
        end = time.time()
        return end - start

    def heapSort(self, data):
        start = time.time()
        N = len(data)
        for i in range(N // 2 - 1, -1, -1):
            heapify(data, N, i)
        for i in range(N - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)
        end = time.time()
        return end - start

    def quickSort(self, data):
        start = time.time()
        quick(data, 0, len(data) - 1)
        end = time.time()
        return end - start

