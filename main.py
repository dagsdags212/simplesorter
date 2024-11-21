from enum import Enum
import sys
from algorithms import *


class SortingAlgorithm(Enum):
    BUBBLE = "bubble"
    MERGE = "merge"
    INSERTION = "insertion"
    QUICK = "quick"
    SELECTION = "selection"


def usage() -> None:
    print("\nSimpleSorter:")
    print("Sort an array using a specific sorting algorithm")
    print("\nUsage: python3 main.py <sorting_algorithn> <numeric_array>")
    print(
        "\nValid sorting algorithms: bubble | merge | insertion | quick | selection\n"
    )


def parse_args() -> tuple[Sorter, NumericIterable]:
    """Validates command line arguments and returns a tuple."""
    if len(sys.argv) != 3:
        usage()
        raise ValueError("arguments cannot be parsed\n")

    algo = sys.argv[1].lower()
    if algo not in SortingAlgorithm:
        usage()
        raise ValueError("invalid sorting algorithm")

    arr = None
    try:
        values = sys.argv[2]
        if "," in values:
            arr = list(map(float, values.replace(" ", "").split(",")))
        elif "|" in values:
            arr = list(map(float, values.replace(" ", "").split("|")))
    except ValueError as err:
        usage()
        raise err

    sorter = None
    if algo and arr:
        match algo:
            case "bubble":
                sorter = BubbleSort()
            case "merge":
                sorter = MergeSort()
            case "insertion":
                sorter = InsertionSort()
            case "quick":
                sorter = QuickSort(randomize=True)
            case "selection":
                sorter = SelectionSort()
        return (sorter, arr)


def main() -> None:
    if len(sys.argv) == 1:
        usage()
        sys.exit(0)

    sorter, arr = parse_args()
    result = sorter(arr)
    print(sorter)
    for num in result:
        print(num)


if __name__ == "__main__":
    main()
