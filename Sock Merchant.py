def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count

n = 9
ar = [10, 10, 10, 10, 20, 20, 20, 30, 50]

result = sockMerchant(n, ar)
print(result)