arr = [4, 3, 2, 1, 3, 5, 5]

def birthdayCakeCandles(l):
    l.pop(0)
    l.sort(reverse = True)
    print(l.count(max(l)))



birthdayCakeCandles(arr)

