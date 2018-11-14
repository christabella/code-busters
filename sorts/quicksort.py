import unittest

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr):
    if len(arr) <= 1:
        return
    pivot = arr[-1]
    pivot_pos = 0  # Where the pivot should go
    for i in arr:
        if arr[i] < pivot:
            swap(arr, i, pivot_pos)
            print(arr)
            pivot_pos += 1  # Pivot is always on the right of smaller elements
    quicksort(arr[:pivot])  # You dummy, doing this is not sorting it in place!
    quicksort(arr[pivot+1:])
    return arr

class Test(unittest.TestCase):
    def test_s(self):
        arr = [0, 3, 1, 2]
        actual = quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
