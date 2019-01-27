def equalizeArray(arr):
    n = len(arr)
    count = 0
    dels = 0
    d = {}
    

    for member in arr:
        print(member)
        if d.__contains__(member):
            occ = d.get(member)
            d[member] = occ + 1
        else:
            d[member] = 1
            
    s = max(d, key=d.get)
    m = d.get(s)
    dels = n - m
#    print(n)
#    print(m)
#    print(dels)
        
    for key,val in d.items():
        print key, val
        
    return dels


arr = [1, 2, 3, 1, 2, 3, 3, 3 ]
#arr = [3, 3, 2, 1, 3]
#arr = [37, 32, 97, 35, 76, 62]
result = equalizeArray(arr)
print result