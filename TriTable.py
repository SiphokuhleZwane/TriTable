# Siphokuhle Zwane
# Complusory Task
# Creating a number period

for i in range(1,10):
    for j in range(1,10):
        if j <= i:                                                 #Statement for when outer loop is less than inner loop
            print(i*j,end = "  ")                                  #Printing all j interval loop outputs in one line 
    print()                                                        #Printing new line for each i interval loop

