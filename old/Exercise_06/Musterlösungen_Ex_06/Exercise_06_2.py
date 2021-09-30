import numpy as np

"""
Simplified Version without loops.
"""

def remove_duplicates(array, percentage=10.):
    array_duplicate = np.unique(array)
    removed_elements = len(array)-len(array_duplicate)
    if (removed_elements*100/len(array) < percentage):
        raise RuntimeError('Failed to remove enough entries!')
    else:
        return array_duplicate, removed_elements

if __name__ == "__main__":
    arr = np.random.randint(1000, size=15000)

    arr_new, diff = remove_duplicates(arr, 20)
    print(arr)
    print(arr_new)
    print(diff)
