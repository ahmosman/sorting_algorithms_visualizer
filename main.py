import sys
import os
import matplotlib.pyplot as plt

from Data import Data
from Sort import Sort

sys.setrecursionlimit(99999999)

def compare_all(sort_obj):
    generator = Data()
    nums = [1000, 2000, 3000, 4000]
    data_names = ["Ascending", "Descending", "V-shaped", "Random", "Constant"]

    sorting_algorithms = [
        ("Insertion Sort", sort_obj.insertionSort),
        ("Selection Sort", sort_obj.selectionSort),
        ("Shell Sort (Sedgewick)", sort_obj.shellSortSedgwick),
        ("Heap Sort", sort_obj.heapSort),
        ("Quick Sort", sort_obj.quickSort),
        ("Quick Sort (Random Pivot)", sort_obj.quickSortRandom),
    ]

    # Create directory for plots if it doesn't exist
    plots_dir = "plots_png"
    os.makedirs(plots_dir, exist_ok=True)

    for sort_name, sorting in sorting_algorithms:
        results = []
        for n in nums:
            times = []
            times.append(sorting(generator.dataInAscendingOrder(n)))
            times.append(sorting(generator.dataInDescendingOrder(n)))
            times.append(sorting(generator.dataAscendingDescendingOrder(n)))
            times.append(sorting(generator.dataRandomOrder(n)))
            times.append(sorting(generator.dataConstant(n)))
            results.append(times)

        results = list(map(list, zip(*results)))  # Transpose for plotting

        plt.figure()
        plt.xlabel('Number of elements')
        plt.ylabel('Time (s)')
        plt.title(sort_name)
        for i, name in enumerate(data_names):
            plt.plot(nums, results[i], label=name)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, f"{sort_name.replace(' ', '_').replace('(', '').replace(')', '').replace('-', '').lower()}.png"))
        plt.close()

if __name__ == "__main__":
    sort = Sort()
    compare_all(sort)