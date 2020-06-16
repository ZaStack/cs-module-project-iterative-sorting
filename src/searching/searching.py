def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] is target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lhs = []
    rhs = []
    # Your code here
    for x in range(len(arr)):
        if arr[x] < target:
            lhs.append(arr[x] < target)
        elif arr[x] > target:
            rhs.append(arr[x] > target)
        elif arr[x] is target:
            return x

    return -1  # not found

