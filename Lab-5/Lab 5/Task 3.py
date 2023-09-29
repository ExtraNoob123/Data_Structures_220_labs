# Task 3
# Printing all elements

def recursive_print(arr):
    if len(arr) == 0:
        print(None)
    elif len(arr) == 1:
        print(arr[0])
    else:
        print(arr[0], end=' ')
        new = []
        for i in range(1, len(arr)):
            new += [arr[i]]
        arr = new
        return recursive_print(arr)


recursive_print([1, 2, 3, 4])
