
def insertionsort_iterative(intlist: list[int]) -> list[int]:
    
    print(f"initial {intlist}")
    lenlist = len(intlist)

    if lenlist <= 1:
        return intlist

    # look at the left side and find the right spot for the element on right (at ith location) 
    # During the process left side is kept sorted at all times until we reach the end of the list 
    # 0th location (left of 1st location) is assumed already sorted since that left side is composed
    # of only 1 element! Therefore we start with a 2nd element at location 1.   
    # We compare our right element (on as part of outer loop) with each element on left side 
    # (as part of inner while loop) until we one which is smaller. 

    # In other words, during each comparison we see whether the element on the left is greater than the element on 
    # the right if it greater it must be moved to the right so we create a 'space' for the right element
    # to go and fit in.
    # Basically we shift all bigger elements (as we do with playing cards) to the right and then
    # place the element (at ith location) at the newly created 'space'!
    for i in range(1, lenlist):
        tmp = intlist[i]
        j = i - 1
        while j >= 0 and intlist[j] > tmp:
            intlist[j+1] = intlist[j]
            j -= 1
        intlist[j+1] = tmp

    return intlist

print("Insertion sorted (iter) ", insertionsort_iterative([10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]))
