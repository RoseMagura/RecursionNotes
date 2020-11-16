def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    return return_permutations(string, 0)

def return_permutations(string, index):
    output = list()
    print('index', str(index))
    
    if index >= len(string):
        print('finished')
        return ['']
    
    small_output = return_permutations(string, index + 1)
    print('small output:')
    print(small_output)
    current_char = string[index]
    print(current_char)

    for subString in small_output:
        for index in range(len(small_output[0]) + 1):
            print(index)
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)
    return output
    
    # if len(string) == 0:
    #     return finalList.append('')
    # else:
    #     first_char = string[0]
    #     after_first = slice(1, None)
    #     rest = string[after_first]
    #     print(rest)
    #     sub_list = permutations(rest)
    #     for a_list in sub_list:
    #         for j in range(0, len(a_list) + 1):
    #             bList = a_list[j] + first_char
    #             finalList.append(bList)
    #     return finalList

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

