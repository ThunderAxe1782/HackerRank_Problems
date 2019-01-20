l = [3, 2, 1, 4, 5]

def miniMaxSum(arr):
    arr.sort()
    minisum = sum(arr[:4])
    maxsum = sum(arr[1:])
    print(minisum)
    print(maxsum)
    print("%s %s" %(minisum, maxsum))

    



miniMaxSum(l)