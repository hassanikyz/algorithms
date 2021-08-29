arr = [10, 7, 6, 4, 9, 3, 8, 5, 2, 0, 1]

def partition(lst, left, right):

    # terminating condition for recursion. If partition is 0 length or the left and right have crossed
    # each other we just return
    if (left >= right):
        return lst

    # choosing very first element as a pivot value against which we will compare other
    # values pointed to by pointers on left and right
    pivotVal = lst[left]

    # use local pointers for left and right since we will need to repartition soon
    i, j = left, right

    # take the values from extreme ends of the array and see if both can be swapped
    # criteria of swap is left side should be greater than pivotVal and right side is less
    # than pivotVal. Keeping moving the left and right towards each other until they cross
    # at which point we need repartition and repeat
    while i <= j:

        # find index of value less than pivotVal
        while (lst[i] < pivotVal):
            i += 1

        # find index of value greater than pivotVal
        while (lst[j] > pivotVal):
            j -= 1

        # if left hasn't crossed right, swap the two
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i +=1
            j -=1

    # repartition into left side and right side and repeat recursively
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
