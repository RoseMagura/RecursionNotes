def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    sum = len(arr) + find(-1, arr, target)
    return sum

def find(index, array, target):
    # base case
    if abs(index) > len(array):
        return -(len(array) + 1)
    if array[index] == target:
        return index
    else:
        return find(index - 1, array, target)

arr = [1, 2, 5, 5, 4]
target = 7
print(last_index(arr, target))