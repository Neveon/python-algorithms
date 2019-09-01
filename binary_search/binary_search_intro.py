# Iterative Binary Search
def binary_search_iterative(data, target):
  # array is already sorted - we split the array in half to find if the target is
  # in the upper half or lower half of the already sorted array
  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2
    print('Indices: low is {}, mid is {}, high is {}'.format(low, mid, high))
    if target == data[mid]:
      return True
    elif target < data[mid]:
      high = mid - 1 # low half with high point of array being below mid
    else:
      low = mid + 1 # upper half, with low point being above mid
  return False

test_arr = [2,3,5,7,8,9,11,13,15,16,21,27,32]
# print(binary_search_iterative(test_arr, 5))




# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
  # Check if low crossed high
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      return binary_search_recursive(data, target, low, mid-1)
    else:
      return binary_search_recursive(data, target, mid+1, high)