import random
import sys

sys.setrecursionlimit(99999999)

def quick(array, start, end, random_pivot=False):
    if start >= end:
        return

    p = partition(array, start, end, random_pivot)
    quick(array, start, p - 1, random_pivot)
    quick(array, p + 1, end, random_pivot)


def calcSedgewick(n):
    return (4 ** (n + 1)) + 3 * (2 ** n) + 1


def sedgewick(n):
    i = 0
    numbers = [1]
    current_sedgewick = calcSedgewick(i)
    while current_sedgewick < n:
        numbers.append(current_sedgewick)
        i += 1
        current_sedgewick = calcSedgewick(i)
    return numbers


def shell(data, k):
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


def partition(data, start, end, random_pivot=False):
    pivot = data[random.randint(start, end)] if random_pivot else data[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and data[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and data[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            data[low], data[high] = data[high], data[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    data[start], data[high] = data[high], data[start]

    return high