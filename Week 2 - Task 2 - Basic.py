def palindrome(Input1):             #checks if a given input is a palindrome
    
    i = 0
    j = -1

    length = len(Input1)
    palindrome = False

    for p in range (length):
        if Input1[i] == Input1[j]:              #checks if end and beg match
            i = i + 1                           #end - 1 and beg + 1
            j = j - 1
            if p == length/2:
                palindrome = True
                break

        else:
            break

    return palindrome

    
