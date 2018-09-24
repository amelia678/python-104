x = 1 
while x < 11:

    y = 1
    while y < 11:
        print("%d X %d = %d" % (x, y, (x * y)))
        y += 1
    x += 1
    print()