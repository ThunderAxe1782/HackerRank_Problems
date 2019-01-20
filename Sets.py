s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}
for _ in range(10):
    method, *args = input().split()
    print(args)
    methods[method](*map(int,args))
    