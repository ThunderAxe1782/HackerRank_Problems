def repeatedString(s, n):
    length = len(s)
    # how many As in the string?
    as_in_string = s.count('a')

    # number of repititions to reach the number of characters
    rep = n / length

    #how many reps are left to complete the number of chars
    rem = n%length * s.count('a')

    count = as_in_string * rep + rem

    print(n % len(s))

    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


    return count


"""    if length == 1 and s == 'a' :
        count = n
    elif s.count('a') == 0:
        return 0
    else:
        for number in range(rep):
            temp += s
        
        count = temp.count('a',0,n+1)
    return count
"""
s = "bab"
n = 10

result = repeatedString(s,n)
#print(result)