def index_equals_value_search(arr):
    # Sorted array -
    # return the first one
    # check arr[i] = i
    #
    left = 0
    right = len(arr) - 1
    mid = int((left + right) / 2)

    while (left <= right):
        if arr[mid] == mid:
            if arr[mid - 1] == mid - 1:
                right = mid - 1
                mid = int(left + right) / 2
            else:
                return mid
        else:
            if arr[mid] > mid:
                right = mid - 1
                mid = int(left + right) / 2
            else:
                left = mid + 1  # left - 2
                mid = int(left + right) / 2  # mid - 2 + 3/2
    return -1


arr1 = [-8, 0, 2, 5]
arr2 = [-1, 0, 3, 6]
arr3 = [-1, 0, 2, 3, 4, 6, 7]
print(index_equals_value_search(arr1))
print(index_equals_value_search(arr2))
print(index_equals_value_search(arr3))
'''
bef|after
   |
   |indices
   |  * - values
   | * -
   |*-
  -* 
- *|
 * |
 01234567
   ^
'''
"""
bs

mid = int(left + right)/2
if arr[mid] == mid:
return mid
else:
if arr[mid] > mid:
  right = mid -1
  mid = int(left + right)/2
else:
  left = mid + 1
  mid = int(left + right)/2





"""
