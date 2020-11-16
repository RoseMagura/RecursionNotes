def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num <= 1:
        return ['']
    elif 1 < num <= 9:
        return list(get_characters(num))
    last_digit = num % 10
    # print()
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)
    output = list()
    print('small output', small_output)
    print('keypad string', keypad_string)
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    return output

print(keypad(23))