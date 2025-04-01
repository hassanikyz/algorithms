arr = [10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]

def bubblesort(intList: list[int]) -> list[int]:

    print("unsorted ", intList)
    listlen = len(intList)

    #Outer loop is to go through all elements in the list 
    for i in range(listlen):

        #after each iteration the largest element reaches it finals position hence loop through only the
        # remaining unsorted ones
        for j in range(0, listlen - 1 - i):
            #look at two consecutive elements and swap if left is greater than right
            if (intList[j] > intList[j+1] ):
                # if left element is greater than right
                # swap
                intList[j], intList[j+1] = intList[j+1], intList[j]
                #print(intList)
 
    return intList

print("Bubble sorted ", bubblesort(arr))
