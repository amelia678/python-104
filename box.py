across = int(input('Width?'))
down = int(input('Height?'))


counter_row = 0

while counter_row < down:
    counter_col = 0
    while counter_col < across:
        
        if counter_row == 0 or counter_row == down - 1 or (counter_col == 0) or (counter_col == (across -1)):
            print('*' , end = '')
        else:
           print(' ', end ='') 
   
                
          
        counter_col = counter_col +1    
    counter_row = counter_row + 1      
    print()         
 





#user input