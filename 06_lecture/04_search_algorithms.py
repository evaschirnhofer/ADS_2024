"""
Linear Search

"""
def search(list, N, key):
    for i in range(0, N):
        if list[i] == key:
            return i
    return -1

list = [2, 3, 4, 10, 40]
N = len(list)
key = 10

result = search(list, N, key)
if(result == -1):
    print("Element is not present in list")
else:
    print("Element is present at index", result)



"""
Binary Search
"""

# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

    while low <= high:
        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

list = [2, 3, 4, 10, 40]
key = 10

# Function call
result = binarySearch(list, 0, len(list)-1, key)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")