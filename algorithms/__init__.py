from collections.abc import Iterable
from time import perf_counter_ns
import random


NumericIterable = Iterable[int] | Iterable[float] | Iterable[int | float]


class Sorter(object):
    def __init__(self) -> None:
        self.time = None
        self.algorithm = None
        self.complexity = None

    def __str__(self) -> str:
        s = f"Sorting algorithm: {self.algorithm}\n"
        s += f"Complexity: {self.complexity}\n"
        if self.time:
            s += f"Elapsed time: {self.time}ns\n"
        return s

    def __call__(self, arr: NumericIterable, time: bool = False) -> NumericIterable:
        if not time:
            return self.sort(arr)
        start = perf_counter_ns()
        sorted_arr = self.sort(arr)
        self.time = perf_counter_ns() - start
        return sorted_arr

    def sort(self, arr: NumericIterable) -> NumericIterable:
        """Implementation of a specific sorting algorithm."""
        raise NotImplemented


class BubbleSort(Sorter):
    """Implementation of the bubble sort algorithm."""

    def __init__(self) -> None:
        super().__init__()
        self.algorithm = "Bubble Sort"
        self.complexity = "O(n^2)"

    def sort(self, arr: NumericIterable) -> NumericIterable:
        nums = arr[:]
        swapping = True
        end = len(nums)
        while swapping:
            swapping = False
            for i in range(1, end):
                if nums[i - 1] > nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[i - 1]
                    nums[i - 1] = tmp
                    swapping = True
            end -= 1
        return nums


class MergeSort(Sorter):
    """Implementation of the merge sort algorithm."""

    def __init__(self) -> None:
        super().__init__()
        self.algorithm = "Bubble Sort"
        self.complexity = "O(n * log(n))"

    def sort(self, arr: NumericIterable) -> NumericIterable:
        def merge_sort(arr: NumericIterable) -> NumericIterable:
            if len(arr) < 2:
                return arr
            left = merge_sort(arr[: len(arr) // 2])
            right = merge_sort(arr[len(arr) // 2 :])
            return merge(left, right)

        def merge(left, right):
            """Combines the elements in the left and right arrays in increase order."""
            final = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    final.append(left[i])
                    i += 1
                else:
                    final.append(right[j])
                    j += 1
            while i < len(left):
                final.append(left[i])
                i += 1
            while j < len(right):
                final.append(right[j])
                j += 1
            return final

        return merge_sort(arr)


class QuickSort(Sorter):
    """Implementation of the quick sort algorithm."""

    def __init__(self, randomize: bool = False) -> None:
        super().__init__()
        self.algorithm = "Quick Sort"
        self.complexity = "O(n * log(n))"
        self.randomize = randomize

    def sort(self, arr: NumericIterable) -> NumericIterable:
        if self.randomize:
            random.shuffle(arr)

        def quick_sort(arr, low, high):
            """Recursively sorts sub-arrays at the left and right of the pivot."""
            if low < high:
                mid = partition(arr, low, high)
                quick_sort(arr, low, mid - 1)
                quick_sort(arr, mid + 1, high)

        def partition(arr, low, high):
            """Moves values less than the pivot to the left, and values greater
            than the pivot to the right."""
            pivot = arr[high]
            i = low
            for j in range(low, high):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[high] = arr[high], arr[i]
            return i

        quick_sort(arr, 0, len(arr) - 1)
        return arr


class InsertionSort(Sorter):
    """Implementation of the insertion sort algorithm."""

    def __init__(self) -> None:
        super().__init__()
        self.algorithm = "Insertion Sort"
        self.complexity = "O(n^2)"

    def sort(self, arr: NumericIterable) -> NumericIterable:
        for i in range(len(arr)):
            curr = i
            while curr > 0 and arr[curr - 1] > arr[curr]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
                curr -= 1
        return arr


class SelectionSort(Sorter):
    """Implementation of the insertion sort algorithm."""

    def __init__(self) -> None:
        super().__init__()

    def sort(self, arr: NumericIterable) -> NumericIterable:
        for i in range(len(arr)):
            smallest = i
            for j in range(smallest + 1, len(arr)):
                if arr[j] < arr[smallest]:
                    smallest = j
            arr[i], arr[smallest] = arr[smallest], arr[i]
        return arr
