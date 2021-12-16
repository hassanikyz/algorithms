####### ITERATIVE SOLUTION #######

# This sort works on the core idea of inserting an element at a particular position after creating a 'space' for it

def insertionsort_iterative(intlist: list[int]) -> list[int]:
    
    print(f"initial {intlist}")
    lenlist = len(intlist)

    if lenlist <= 1:
        return intlist

    # Look at the left side and find the correct spot for the element on the right (at ith location). 
    # During the process left side is kept sorted at all times until we reach the end of the list. 
    # 0th location (left of 1st location) is assumed already sorted since that left side is composed
    # of only 1 element! Therefore we start with a 2nd element at location 1.   
    # We compare each right element (as part of outer loop) with each element on left side 
    # (as part of inner while loop) until we find a smaller right element (candidate to move to left). 

    # In other words, during each comparison we see whether elements on the left are greater than the element on 
    # the right. If left is greater it must be shifted over to the right so we create a 'space' for the right element
    # to go and fit in.
    # Basically we shift all bigger elements (as we do with playing cards) to the right and then
    # place the element (at ith location) at the newly created 'space'!
    for i in range(1, lenlist):
        tmp = intlist[i]
        j = i - 1
        while j >= 0 and intlist[j] > tmp:
            #shift left element to the right
            intlist[j+1] = intlist[j]
            j -= 1
        intlist[j+1] = tmp

    return intlist

print("Insertion sorted (iter) ", insertionsort_iterative([10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]))

####### RECURSIVE SOLUTION #######
def insertionsort_recursive(intlist: list[int], listlen) -> list[int]:

    print(f"Initial List {intlist[0:listlen]}")
    if (listlen <= 1):
        return intlist
    
    # first solve it for a smaller list
    insertionsort_recursive(intlist, listlen - 1)

    # now (assuming everything on the left is sorted) take the last element and place it in its correct position
    # take the last element and start searching for its correct location inside the already sorted list
    location_lastElement = listlen - 1
    lastElement = intlist[location_lastElement]

    #location of one element left of last element
    j = location_lastElement - 1
    
    #keep shifting elements to the right overwriting last element as well. 
    #shifting elements to the right eventually creates 'space' for the lastElement on the left to go and fit in.
    while j >=0 and intlist[j] > lastElement:
        
        intlist[j + 1] = intlist[j]
        print(f"After shift {intlist[0:listlen]}")
        j -= 1

    #location found, now fit it in there!
    intlist[j+1] = lastElement

    print(f"After fitting in lastElement {lastElement}, {intlist[0:listlen]}")
    return intlist

print("Insertion sorted (recursively) ", insertionsort_recursive([10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1], len([10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1])))


