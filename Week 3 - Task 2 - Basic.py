def linear(Target):                                                           #performes a linear search on a given list
    list = [3, 7, 2, 9, 4, 23, 45, 76, 45, 46, 56, 6, 4, 34, 5, 56]     #the given list
    length = len(list)
    position = 0
    

    try:

        while position <= length -1:                                        #compares target value with values in list to find a match
            if list[position] == Target:
                return True
            if position == length -1:
                return False   
            else:
                position += 1

    except:
        print("Target is invalid")              #input validation

