counter_col = 0
counter_row = 0

while counter_row < 4:
    while counter_col < 7:
        if counter_row == 0:
            print(' ' * 3, '*', ' ' * 3, end = '')
        elif counter_row == 1:
            print(' ' * 2, '*' * 3, ' ' * 2, end = '')
        elif counter_row == 2:
            print(' ', '*' * 5, ' ', end = '')
        elif counter_row == 3:
            print('*' * 7, end = '')
            counter_col = counter_col + 1
        counter_row = counter_row + 1           
      