def jumpingOnClouds(c):
    jumps = 0
    i = 0
    n = len(c)
    while i < n:
        print('i = %s'%i)
        if i == n-1:
            
        if (c[i+2] == 0) and (i+2 < n):
                jumps += 1
                i += 2
        else:
                jumps += 1
                i = i + 1
    return jumps 

c = [0, 0, 1, 0, 1, 0, 0] 
result = jumpingOnClouds(c)
print(result)