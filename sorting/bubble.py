arr = [10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]

def bubblesort(intList: list[int]) -> list[int]:

    print("unsorted ", intList)
    listlen = len(intList)

    #loop to do this 
    for i in range(1, listlen):
        for j in range(1, listlen):
            if (arr[listlen - j] < arr[listlen - 1 - j]):
                arr[listlen - j], arr[listlen - 1 - j] = arr[listlen - 1 - j], arr[listlen - j]
                #print(arr)
 
    return intList

print("Bubble sorted ", bubblesort(arr))
