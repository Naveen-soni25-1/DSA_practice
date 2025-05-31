def recursive_max(arr):
    """A recursive funftion to find maximum number."""
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] >= recursive_max(arr[1:]):
        return arr[0]
    else:
        return recursive_max(arr[1:])
    
my_arr = [1, 24, 45, 100, 34, 45]
print(recursive_max(my_arr))