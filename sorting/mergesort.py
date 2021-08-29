def mergeBothLists(left: list[int], right: list[int]):
    # print(f"left {left}, right {right}")

    # left list iterator
    i = 0
    # right list iterator
    j = 0

    # create an empty list which will have merged data from both right and left
    mergedList = []

    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            mergedList.append( left[i])
            i += 1
            
        elif left[i] > right[j]:
            mergedList.append(right[j])
            j += 1
        
    # we don't know which of the two lists was shorter so best to take the remaining (if any) elements and simply 
    # add them to the mergedList to get the final output
    mergedList += left[i:]
    mergedList += right[j:]
    
    return mergedList

def mergesort(original: list[int]):
    listlen = len(original)
    if (listlen <= 1):
        return original

    # Step 1: split the list into rough halves
    # Step 2: run mergesort (recursively) on both halves one by one
    # Step 3: merge the two sorted lists together 


    # Step 1
    mid  = len(original)//2
    left = original[:mid]
    right = original[mid:]

    # Step 2  (recursion)
    left = mergesort(left)
    right = mergesort(right)

    # Step 3
    sorted = mergeBothLists(left, right)

    return sorted
