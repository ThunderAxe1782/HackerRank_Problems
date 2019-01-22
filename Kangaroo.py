def kangaroo(x1, v1, x2, v2):
    y = 0 # number of jumps

    if ((x2 > x1) and (v2 > v1)) or ((x1 > x2) and (v1 > v2)) or ((x1 != x2) and (v1 == v2)):
        return "NO"
    else:
        if (x1 - x2) % (v2 - v1) == y:
            return "YES"
        return "NO"
        

x1 = 43
v1 = 2
x2 = 70
v2 = 2

result = kangaroo(x1, v1, x2, v2)
print(result)