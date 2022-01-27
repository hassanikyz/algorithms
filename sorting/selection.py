def selection_sort(originalist: list[int]):
    
    listlen = len(originalist)

    # It is called selection sort, because it repeatedly selects the next-smallest element and swaps it into place
    
    # Go through the entire list look for a minimum value (smallest). Once min val is found swap it with
    # the very first element of the remaining unsorted elements.
    
    # In the beginning the very first element is obviously supposed to be placed at the 0th location.
    # As smallest values are placed in their correct locations the size of the unsorted list shrinks.
    
    
    for i in range(listlen):
        minval_idx = i
        for j in range(i+1, listlen):
            if originalist[j] < originalist[minval_idx]:
                #found a new min? Update the index 
                minval_idx = j

        #pythonic way of swapping the first element of unsorted bunch with the newly found min value    
        originalist[i], originalist[minval_idx] = originalist[minval_idx], originalist[i]

    return originalist

print(f"Calling selection sort {selection_sort([10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1])}")
## output ###
## Initial List is [10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]
## Calling selection sort [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
