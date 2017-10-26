def linear():                                                           #performes a linear search on a given list
    list = [3, 7, 2, 9, 4, 23, 45, 76, 45, 46, 56, 6, 4, 34, 5, 56]     #the given list
    length = len(list)
    position = 0
    


    while position <= length -1:                                        #compares target value with values in list to find a match
        if list[position] == Target:
            print("Found")
            return
        if position == length -1:
            print("Not Found")
            return
            
        else:
            position += 1




Target = int(input("Enter the target: "))
linear()
