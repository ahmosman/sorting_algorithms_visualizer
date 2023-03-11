
import sys

import matplotlib.pyplot as plt

from Data import Data
from Sort import Sort

sys.setrecursionlimit(99999999)

# print(shell_sort([4,14,7,2,1,10,3,8,11,5,12],5))


# data = data_gen.dataConstant(100000)
# print(sort.insertionSort(data))
# data = dataAscendingDescendingOrder(500)
# print(quickSort(data, 0, len(data) - 1)) # moge dopisac False obok

# podzial na klasy, czas, generowanie wszystkiego po wszystkim

def compare(sorting):
    generator = Data()
    nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    data_names = ["rosnący", "malejący", "V-kształtny", "losowy", "stały"]
    results = []
    for i in nums:
        times = []
        time = sorting(generator.dataInAscendingOrder(i))
        times.append(time)
        time = sorting(generator.dataInDescendingOrder(i))
        times.append(time)
        time = sorting(generator.dataAscendingDescendingOrder(i))
        times.append(time)
        time = sorting(generator.dataRandomOrder(i))
        times.append(time)
        time = sorting(generator.dataConstant(i))
        times.append(time)
        results.append(times)

    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas (s)')
    plt.title(sorting.__name__)
    plt.plot(nums, results)
    plt.legend(data_names)
    plt.show()


data_gen = Data()
sort = Sort()
compare(sort.selectionSort)
# data = data_gen.dataInAscendingOrder(2500)
# sort.quickSort(data)
# print(data)

# time = sort.insertionSort(data_gen.dataConstant(10000))
# print(time)
