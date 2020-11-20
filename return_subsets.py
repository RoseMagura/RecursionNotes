def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]
    
    small_output = return_subsets(arr, index + 1)
    output = list()

    for element in small_output:
        output.append(element)
    
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = subsets(arr)
        
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")    

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)