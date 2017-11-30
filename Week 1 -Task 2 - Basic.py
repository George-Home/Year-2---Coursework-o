
def Armstrong_Chk (user_number):   #function to check if a given number is also an armstrong number
    
    Total = 0

    try:
    
    #user_number = int(input("Enter your number: "))     #requests a number to test from the user           #removed for unit test
        number_s = str(user_number)                         #converts given number into a string
        length_num = len(number_s)                          #finds the length of the given number

        for i in number_s:                                  #finds the sum of the cubes of its digits
            Total += int(i) ** length_num

        if user_number == Total:                            #prints output if the number is an armstrong number or not
        #print(number_s + " is a armstrong number... yay")
            output1 = True
            return output1
        else:
        #print(number_s + " is not an armstrong number")
            return output1

    except:
        print("Enter an appropriate number")        #input validation

#Armstrong_Chk(user_number)
