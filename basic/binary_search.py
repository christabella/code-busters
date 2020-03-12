"""
Find the point at which index == value
  point
  bef|after
     |
     |indices
     |   *
     |  *  - values
     | * -
     |*-
    -* 
  - *|
-  * |
  *  |
 *   |
*    |
 0123456
   ^
"""


def index_equals_value_search(arr):
    n = len(arr)
    l, r = 0, n  # Range is [l, r)]
    while l < r:
        print(l, r)
        mid = (l + r) // 2  # Round down
        print(mid)
        diff = arr[mid] - mid
        if (diff < 0):  # Increase to find 0
            l = mid + 1
        elif (diff == 0):
            prev_diff = arr[mid - 1] - (mid - 1)
            if (mid == 0) or (prev_diff < 0):
                return mid
            else:
                r = mid
        else:
            r = mid
    return -1


# if __name__ == '__main__':
#   print(index_equals_value_search([1, 2, 3, 4]))
print(index_equals_value_search([1, 2, 3, 4, 4]))
print(index_equals_value_search([-5, 0, 2, 3, 10, 29]))
