arr = [10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]

def partition(lst, left, right):

    if (left >= right):
        return lst

    pivotVal = lst[left]
    i, j = left, right
    while i <= j:

        while (lst[i] < pivotVal):
            i += 1

        while (lst[j] > pivotVal):
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i +=1
            j -=1

    if (left < j):
        partition(lst, left, j)
    if (i < right):
        partition(lst, i, right)

    return lst



def quicksort(lst: list[int]):
    print(f"quicksort the list {lst}")
    partition(lst, 0, len(lst) - 1)
    print(f"sorted {lst}")
    return lst
