def rec_binary_search(arr, item, low=0, high=None):
    """Correct binary search using recursion with index tracking."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1  # item not found

    mid = (low + high) // 2

    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return rec_binary_search(arr, item, low, mid - 1)
    else:
        return rec_binary_search(arr, item, mid + 1, high)

my_arr = [1, 3, 45 ,65 ,90, 234]   
item = 45 
index = rec_binary_search(my_arr, item)
if index !=1:
    print(f"item found at index:{index}")
else:
    print("Item not found")