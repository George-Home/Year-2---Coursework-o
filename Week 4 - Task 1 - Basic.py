sequenceb = [2,7,9,4,1,5,3,6,0,8]
sequencei = [2,7,9,4,1,5,3,6,0,8]
sequences = [2,7,9,4,1,5,3,6,0,8]

###Bubble Sort###
def bubbleSort(sequenceb):                         #sequence is added into function otherwise it will keep changing the original each iteration
    print("Bubble Sort")
    for ordered in range(len(sequenceb)-1,0,-1):   #breaks when list is ordered
        for i in range (ordered):
            if sequenceb[i] > sequenceb[i+1]:       #measures each pair in line and swaps them where necessary
                holder = sequenceb[i]
                sequenceb[i] = sequenceb[i+1]
                sequenceb[i+1] = holder
 
                print(sequenceb)                   #prints the sequence every time a value is changed


bubbleSort(sequenceb)


###Insertion Sort###
def insertionSort(sequencei):
    print("Insertion Sort")
    
    for p in range(1,len(sequencei)):                           #assigns the position to mark how far throught the sequence
        position = sequencei[p]                                 #holder is the current pointer between the position and start of the sequence
        holder = p

        while position < sequencei[holder - 1] and holder > 0:  #true until the holder reaches the start of the sequence and a swap is needed
            sequencei[holder] = sequencei[holder-1]                 
            holder -=1                                          #holder decreases by 1 and moves back a position in the sequence
        sequencei[holder] = position
        print(sequencei)
               

insertionSort(sequencei)

###Selection Sort###
def selectionSort(sequences):
    print("Selection Sort")
    for i in range(len(sequences)-1,0,-1):                      #outer loop to run until all values are repositioned
        maximum = 0
        for j in range(1, i+1):                                 #finds the largest value in the sequence
            if sequences[j] > sequences[maximum]:
                maximum = j
                
        holder = sequences[i]                                   #swaps largest value at end of sequence that hasnt already been sorted
        sequences[i] = sequences[maximum]
        sequences[maximum] = holder
        print(sequences)

selectionSort(sequences)

#Bubble sort had 23 element moves
#Insertion sort had 7 element moves
#Selection sort had 8 element moves
#Insertion is the best sorting method for these integers
#the  worst configuration would be back to front - [9,8,7,6,5,4,3,2,1,0]
   
    
