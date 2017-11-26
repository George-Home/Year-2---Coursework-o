def palindrome():
    i = 0
    j = -1
    Input1 = [1,3,6,6,3,1]

    length = len(Input1)
    palindrome = False

    for p in range (length):
        if Input1[i] == Input1[j]:              #checks if end and beg match
            i = i + 1                           #end - 1 and beg + 1
            j = j - 1
            if p == length/2:
                print("This is a palindrome")
                break

        else:
            print("not a palindrome")
            break

    
palindrome()
