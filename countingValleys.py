def countingValleys(n, s):
    valleys = 0
    height = 0
    for char in s:
        if char == 'U': height += 1
        else: height -= 1

        if (height == 0) & (char == 'U'): valleys += 1

    return valleys   


n = 8
s = input()

result = countingValleys(n, s)
print(result)