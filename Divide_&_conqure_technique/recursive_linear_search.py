def rec_linear_search(arr, item):
    """ A recursive linear search """
    if not arr:
        return -1  # Item not found
    if arr[0] == item:
        return 0
    else:
        res = rec_linear_search(arr[1:], item)
        return res + 1 if res != -1 else -1

# Test
my_arr = [1, 10, 24, 56, 75, 3, 45, 2254]
index = rec_linear_search(my_arr, 56)
if index != -1:
    print(f"Item found at index: {index}")
else:
    print("Item not found")
