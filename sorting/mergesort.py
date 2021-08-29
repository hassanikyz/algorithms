def mergeBothLists(left: list[int], right: list[int]):
    # print(f"left {left}, right {right}")
    i = 0
    j = 0
    mergedList = []
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            mergedList.append( left[i])
            i += 1
            
        elif left[i] > right[j]:
            mergedList.append(right[j])
            j += 1
        
    mergedList += left[i:]
    mergedList += right[j:]
    
    # print(f"mergeBothLists: Merged List {mergedList}")
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
