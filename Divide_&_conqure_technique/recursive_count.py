def recursive_count(arr):
    """A recursive function to count"""
    if not arr:
        return 0
    return 1 + recursive_count(arr[1:])

my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_count(my_arr))