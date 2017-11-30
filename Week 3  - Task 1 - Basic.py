def mirror(U_input):                                           #mirroring function
    placeholder = ""                                    #placeholder for the final output
    position = len(U_input)                             #finds the length of the given input

    try:
    
        for i in range (position):                          #position decreases as each letter is added to the placeholder
            position = position -1
            placeholder = placeholder + U_input[position]

    except:
        print("Not a valid input")              #input validation


### Time Complexity (queue): O(n) ###


