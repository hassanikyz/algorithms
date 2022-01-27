# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
mlist = [10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
def bubble_sort(mlist):
    #print(mlist)
    for i in range(len(mlist)):
        print(mlist)
        for j in range(0, len(mlist) - i - 1 ):
            if (mlist[j] > mlist[j+1]):
                mlist[j], mlist[j+1] =  mlist[j+1], mlist[j]
    
    return mlist
  
def selection_sort(mlist):
    #print(mlist)
    for i in range(len(mlist)):
        print(mlist)
        min_idx = i
        for j in range(i+1, len(mlist)):
            if mlist[min_idx] > mlist[j]:
                min_idx = j
        
        mlist[i], mlist[min_idx] = mlist[min_idx], mlist[i]
    return mlist
print("Using bubble sort")
print(bubble_sort(mlist))
mlist = [10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
print("Using selection sort")
print(selection_sort(mlist))
mlist = [10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
def insertion_sort(mlist):
    
    
    for i in range(1, len(mlist)):
        print(mlist)
        e = mlist[i]
        j = i - 1
        while j>=0 and mlist[j] > e:
            mlist[j+1] = mlist[j]
            j = j - 1
        mlist[j+1] = e
        
    return mlist
print("Using Insertion sort")
print(insertion_sort(mlist))
        
                

##########################
"""
Using bubble sort
[10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
[9, 0, 6, 2, 4, 8, 3, 7, 5, 1, 10]
[0, 6, 2, 4, 8, 3, 7, 5, 1, 9, 10]
[0, 2, 4, 6, 3, 7, 5, 1, 8, 9, 10]
[0, 2, 4, 3, 6, 5, 1, 7, 8, 9, 10]
[0, 2, 3, 4, 5, 1, 6, 7, 8, 9, 10]
[0, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10]
[0, 2, 3, 1, 4, 5, 6, 7, 8, 9, 10]
[0, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Using selection sort
[10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
[0, 9, 10, 6, 2, 4, 8, 3, 7, 5, 1]
[0, 1, 10, 6, 2, 4, 8, 3, 7, 5, 9]
[0, 1, 2, 6, 10, 4, 8, 3, 7, 5, 9]
[0, 1, 2, 3, 10, 4, 8, 6, 7, 5, 9]
[0, 1, 2, 3, 4, 10, 8, 6, 7, 5, 9]
[0, 1, 2, 3, 4, 5, 8, 6, 7, 10, 9]
[0, 1, 2, 3, 4, 5, 6, 8, 7, 10, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Using Insertion sort
[10, 9, 0, 6, 2, 4, 8, 3, 7, 5, 1]
[9, 10, 0, 6, 2, 4, 8, 3, 7, 5, 1]
[0, 9, 10, 6, 2, 4, 8, 3, 7, 5, 1]
[0, 6, 9, 10, 2, 4, 8, 3, 7, 5, 1]
[0, 2, 6, 9, 10, 4, 8, 3, 7, 5, 1]
[0, 2, 4, 6, 9, 10, 8, 3, 7, 5, 1]
[0, 2, 4, 6, 8, 9, 10, 3, 7, 5, 1]
[0, 2, 3, 4, 6, 8, 9, 10, 7, 5, 1]
[0, 2, 3, 4, 6, 7, 8, 9, 10, 5, 1]
[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
