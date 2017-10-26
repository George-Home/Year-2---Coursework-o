def Armstrong_Chk ():   #function to check if a given number is also an armstrong number
    
    Total = 0           
    
    user_number = int(input("Enter your number: "))     #requests a number to test from the user
    number_s = str(user_number)                         #converts given number into a string
    length_num = len(number_s)                          #finds the length of the given number

    for i in number_s:                                  #finds the sum of the cubes of its digits
        Total += int(i) ** length_num

    if user_number == Total:                            #prints output if the number is an armstrong number or not
        print(number_s + " is a armstrong number... yay")
    else:
        print(number_s + " is not an armstrong number")

    



Armstrong_Chk()


###############testing notes - write small algorithm to count to a given number and output any armstrong numbers
