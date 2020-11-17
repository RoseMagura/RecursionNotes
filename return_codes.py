asciiDict = {(i - 96): chr(i) for i in range(97, 122)}
final = []
def all_codes(number, x, final):
    if (number // x) == 0:
        return 

    if(26 > number % x > 0):
        entry = asciiDict.get(number // x, '') + asciiDict.get(number % x, '')
        print(entry)
        final.append(entry)

    elif(number // x > 1):
        letters = []
        for digit in str(number // x):
            letters.append(asciiDict.get(int(digit), ''))
        final.append(''.join(letters))
        print(letters)
    all_codes(number, x * 10, final)
    return


print(all_codes(4545, 1, final))
print('final', str(final))