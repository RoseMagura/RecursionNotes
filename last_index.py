def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    return last_index_arr(arr, target, len(arr) - 1)

def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    if arr[index] == target:
        return index
    return last_index(arr, target, index - 1)

arr = [1, 2, 5, 5, 4]
target = 7
print(last_index(arr, target))