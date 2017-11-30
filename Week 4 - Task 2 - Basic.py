def binarySearch(value):
    maxValue = 20000
    midValue = 10000
    minValue = 0
    found = False

    while found == False:
        try:
            if value > maxValue or value < minValue:            #input validation
                print("value given is out of range")
                break
            midValue = int(((maxValue - minValue) / 2) + minValue)                                      #calculates the current middle value
            if midValue == value:                                                                       #checks if it has found your value
                found == True
                print("Guessed it!")
                return True
                break
            check = input("Is your answer {}? Press h for higher or l for lower: " .format(midValue))     
            if check == "h":                                                                            #if value is higher - the minimum is adjusted to remove null values
                minValue = midValue
            elif check == "l":                                                                          #if value is lower - the maximum is adjusted to remove null values
                maxValue = midValue
            else:
                print("This is an incorrect value")         #input validation
        except:
            print("the value given is incorrect")


#value = int(input("Enter a number between 1 and 20000: "))
#binarySearch(value) 
