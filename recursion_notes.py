def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n - 1)

def reverse_string(input):
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        print(sub_string)
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char

# print(reverse_string("") == "")
# print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]
        sub_input = slice(1, -1) # or input[1:-1]
        # if first_char == last_char:
        #     return is_palindrome(input[remaining])
        # else:
        #     return False
        return (first_char == last_char) and is_palindrome(sub_input)
        
print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
