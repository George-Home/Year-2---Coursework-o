def mirror():                                           #mirroring function
    placeholder = ""                                    #placeholder for the final output
    position = len(U_input)                             #finds the length of the given string

    
    for i in range (position):                          #position decreases as each letter is added to the placeholder
        position = position -1
        placeholder = placeholder + U_input[position]

    print (placeholder)


U_input = str(input("Enter the string: "))

mirror()
