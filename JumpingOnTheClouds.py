def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0

    while i < n-1:
        print('i = %s' %i)
        if (i+2 < n) and (c[i+2] != 1):
            jumps += 1
            i += 2
        else:
            jumps += 1
            i += 1
            
    return jumps


c = [0, 0, 0, 1, 0, 0]
result = jumpingOnClouds(c)
print(result)