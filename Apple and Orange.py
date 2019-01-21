def countApplesAndOranges(s, t, a, b, apples, oranges):
    sam = 0
    # calculating apples
    for apple in apples:
        apple_drop_location = apple + a
        if apple_drop_location >= s and apple_drop_location <= t:
            sam += 1
    print(sam)
    sam = 0
    for orange in oranges:
        orange_drop_location = orange + b
        if orange_drop_location <= t and orange_drop_location >= s:
            sam += 1
    print(sam)

s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]

countApplesAndOranges(s, t, a, b, apples, oranges)
    

