def recursive_sum(arr):
    """A recursive function for sum"""
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])

my_arr = [1, 2, 3, 55, 55, 64, 97540058]
print(recursive_sum(my_arr))