"""In-place sorting with O(log n) to O(n^2) time, and  O(log n) memory"""

import unittest
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, l=0, r=None):
    """Recursively partition array's elements in-place w.r.t. a chosen pivot.

    Put smaller (or equal) values to the left of pivot, and greater to the right.

    Args:
      arr: Array of numbers
    """
    if r is None: r = len(arr)
    if l >= r-1:
        return
    pivot = arr[r-1]  # Use last element as pivot
    pivot_pos = l  # Where the pivot should go; intialize at the head
    for i in range(l, r-1):  # The actual partitioning
        if arr[i] <= pivot:
            swap(arr, i, pivot_pos)
            pivot_pos += 1  # Pivot is always on the right of smaller elements
    # Put the pivot where it should go
    swap(arr, pivot_pos, r-1)
    quicksort(arr, l=l, r=pivot_pos)
    quicksort(arr, l=pivot_pos, r=r)
    return arr


class Test(unittest.TestCase):
    random.seed(10)
    def test(self):
        arr = [0, 3, 1, 2]
        actual = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)
    def test_10(self):
        arr = [random.randint(-100, 100) for i in range(10)]
        actual = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)
    def test_1000(self):
        arr = [random.randint(-100, 100) for i in range(1000)]
        actual = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
