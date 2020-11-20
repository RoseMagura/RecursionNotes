combos = list()
def subsets(combos, arr):
    index = 0 
    return find_permutations(combos, arr, 0)


def find_permutations(combos, arr, index):
    # base case
    if index >= len(arr):
        combos.append([])
        return combos

    sub = list()
    sub.append(arr[index])
    combos.append(sub)

    available = arr[index + 1:]
    for digit in available:
        if [arr[index], digit] not in combos:
            combos.append([arr[index], digit])

    if arr[index :] not in combos:
        combos.append(arr[index :])
    small_output = find_permutations(combos, arr, index + 1)
    return combos

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

print(sorted(subsets(combos, arr)) == sorted(solution))
