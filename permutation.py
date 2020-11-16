import copy 

def permute(list):
    finalCompoundList = []
    # add permutations to all
    if len(list) == 0:
        finalCompoundList.append([])
    else:  
        first_element = list[0]
        after_first = slice(1, None)
        rest_list = list[after_first]
        sub_compoundList = permute(rest_list)  
        
        for aList in sub_compoundList:
            for j in range(0, len(aList) + 1):
                bList = copy.deepcopy(aList)     
                bList.insert(j, first_element)
                finalCompoundList.append(bList)
    return finalCompoundList              

# Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

# print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
# print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")