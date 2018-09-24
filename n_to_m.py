#what i've got:
    #the abilty to ask user for start/end loop values
#what i want:
    # to create a loop with user's start/end input
#how to i get:
    #create a while loop that starts at user's start number and ends at end integer   
start_number = int(input("Enter a number to start the loop"))
end_number = int(input("Enter a number to end the loop"))

while start_number <= end_number:
    print(start_number)
    start_number = start_number + 1

print() 