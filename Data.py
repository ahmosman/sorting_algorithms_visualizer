import random
import sys

sys.setrecursionlimit(99999999)

class Data:
    def dataInAscendingOrder(self, N):
        data = []
        for i in range(1, N + 1):
            data.append(i)
        return data

    def dataInDescendingOrder(self, N):
        data = []
        for i in range(N, 0, -1):
            data.append(i)
        return data

    def dataAscendingDescendingOrder(self, N):
        odd_numbers = [i for i in range(1, N + 1) if i % 2 != 0]
        even_numbers = [i for i in range(N, 0, -1) if i % 2 == 0]
        return odd_numbers + even_numbers

    def dataRandomOrder(self, N):
        data = []
        for i in range(N):
            number = random.randint(1, N)
            data.append(number)
        return data

    def dataConstant(self, N):
        data = []
        number = random.randint(1, N)
        for i in range(N):
            data.append(number)
        return data