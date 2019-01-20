order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

s = "Sorting1234"
b = ''.join(sorted(s, key=order.index))
#b = sorted(s, )
print(str(b))
