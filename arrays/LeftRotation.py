def rotLeft(a, d):
    temp = 0

    for num in range(d):
        temp = a.pop(0)
        a.append(temp)

    return(a)





a = [1, 2, 3, 4, 5]
d = 4

result = rotLeft(a, d)
print(result)
