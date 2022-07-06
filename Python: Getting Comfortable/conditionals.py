n = 54                                  
if n % 2 == 1:                           # if "n" is odd
    print('Weird')
elif n % 2 == 0 and n in range(2, 6):    # if "n" is even AND in the range of 2 to 5
        print('Not Weird')
elif n % 2 == 0 and n in range(6, 21):   # if "n" is even AND in the range of 6 to 20
        print('Weird')
else:
    if n % 2 == 0 and n > 20:            # if "n" is even AND is greater than 20 
        print('Not Weird')
