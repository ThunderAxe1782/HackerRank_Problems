arr = [4, 3, 2, 1, 3, 5, 5]

def birthdayCakeCandles(l):
    print(l)
    l.pop(0)
    print(l)
    l.sort(reverse = True)
    print(l)
    print(max(l))
    print(l.count(max(l)))



birthdayCakeCandles(arr)