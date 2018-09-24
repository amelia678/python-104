number_of_coins = -1 
want_another = 'yes'

while want_another == 'yes':
    number_of_coins = number_of_coins + 1
    print('You have %d coins' % (number_of_coins))
    want_another = input('Do you want another?')
print('Bye')    
