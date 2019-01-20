"""with open("nested_lists_input.txt", "r") as inputfile:
    n = inputfile.read()
    lines = n.splitlines()
    print(lines)
    """
d = {}
l = []

with open("nested_lists_input.txt", "a") as f:
    next(f)
    for line in f:    
        print(line)
        key1 = line
        d.update()

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))