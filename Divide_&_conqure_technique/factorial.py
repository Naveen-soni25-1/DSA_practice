def fact(x):
    """A function to do factorial"""
    if x == 1:
        return 1
    return x * fact(x - 1)

print(fact(5))