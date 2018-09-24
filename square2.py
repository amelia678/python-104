N = int(input('How big is the square'))
counter_row = 0
while counter_row < N:
    counter_col = 0 
    while counter_col < N:
        print('*', end ='')
        counter_col = counter_col + 1
    counter_row = counter_row + 1
    print()

