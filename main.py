import random
import sys
import time
#import matplotlib
#import matplotlib.pyplot as plt
sys.setrecursionlimit(99999999)

class DataGenerate:
    def dataInAscendingOrder(self, N):
        data = []
        for i in range(1, N+1):
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

class Sort:
    def insertionSort(self, data):
        start = time.time()
        for i in range(1,len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        end = time.time()
        return end-start

    def selectionSort(self, data):
        start = time.time()
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index  = j
            data[i], data[min_index] = data[min_index], data[i]
        end = time.time()
        return end-start

    def shellSortSedgwick(self, data):
        start = time.time()
        sedgewick_reversed = sedgewick(len(data))[::-1]
        for k in sedgewick_reversed:
            data = shellSort(data, k)
        end = time.time()
        return end-start

    def heapSort(self, data):
        start = time.time()
        N = len(data)
        for i in range(N // 2 - 1, -1, -1):
            heapify(data, N, i)
        for i in range(N - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)
        end = time.time()
        return end-start

    def quickSort(self, data, low, high, random_pivot = False):
        start = time.time()
        if low < high:
            q = partition(data, low, high, random_pivot)
            quickSort(data, low, q, random_pivot)
            quickSort(data, q + 1, high, random_pivot)
        end = time.time()
        return end-start


def calcSedgewick(n):
    return (4 ** (n + 1)) + 3 * (2 ** (n)) + 1

def sedgewick(n):
    i = 0
    numbers = [1]
    current_sedgewick = calcSedgewick(i)
    while current_sedgewick < n:
        numbers.append(current_sedgewick)
        i += 1
        current_sedgewick = calcSedgewick(i)
    return numbers

def shellSort(data, k):
    for gap in range(k):
        for i in range(k + gap, len(data), k):
            key = data[i]
            j = i - k
            while j >= gap and data[j] > key:
                data[j + k] = data[j]
                j -= k
            data[j + k] = key
    return data

def heapify(data, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < N and data[largest] < data[l]:
        largest = l
    if r < N and data[largest] < data[r]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, N, largest)

def partition(data, low, high, random_pivot=False):
    pivotek = data[random.randint(low, high)] if random_pivot else data[low]
    i = low
    j = high
    while True:
        while data[i] < pivotek:
            i += 1
        while data[j] > pivotek:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
        else:
            if j == high:
                j -= 1
            return j


#print(shell_sort([4,14,7,2,1,10,3,8,11,5,12],5))


#data = data_gen.dataConstant(100000)
#print(sort.insertionSort(data))
#data = dataAscendingDescendingOrder(500)
#print(quickSort(data, 0, len(data) - 1)) # moge dopisac False obok

# podzial na klasy, czas, generowanie wszystkiego po wszystkim

def compare(sorting):
    data_gen = DataGenerate()
    nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    data_names = ["rosnący", "malejący", "V-kształtny", "losowy", "stały"]
    results = []
    for i in nums:
        times = []
        time = sorting(data_gen.dataInAscendingOrder(i))
        times.append(time)
        time = sorting(data_gen.dataInDescendingOrder(i))
        times.append(time)
        time = sorting(data_gen.dataAscendingDescendingOrder(i))
        times.append(time)
        time = sorting(data_gen.dataRandomOrder(i))
        times.append(time)
        time = sorting(data_gen.dataConstant(i))
        times.append(time)

        results.append(times)
    plt.plot(nums, results)
    plt.show()

data_gen = DataGenerate()
sort = Sort()
#compare(sort.insertionSort)

time = sort.insertionSort(data_gen.dataConstant(10000))
print(time)
