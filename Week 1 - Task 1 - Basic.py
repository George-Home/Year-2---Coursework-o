#combining strings :o
def string_join ():
    position = 0                #keeps track of the pointer along the string
    Str_3 = ""                  #placeholder for end result

    #checks which string is longer and saves the extra characters to its own variable
    if len(Str_1) > len(Str_2):
        count = len(Str_2)
        extra = (Str_1[count:])
    else:
        count = len(Str_1)
        extra = (Str_2[count:])

    #adds each letter from both strings together one character at a time
    while count > position :

        Str_3 = (Str_3 + Str_1[position] + Str_2[position])
        
        position = position + 1
    #prints the end result    
    print(Str_3 + extra)        


#input for both strings
Str_1 = str(input("Enter the first string: "))
Str_2 = str(input("Enter the second string: "))
#runs the string combine function
string_join () 
