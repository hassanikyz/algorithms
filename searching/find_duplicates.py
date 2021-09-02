def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    ### hashtable or dictionary in python with key as digit and value as number of times it appeared
    ### At the end we will traverse the dictionary and produce the result list
    mydict = {}
    for x in lst:
        if x in mydict:
            mydict[x] += 1
        else:
            mydict[x] = 1
            
    for y in mydict:
        if mydict[y] > 1:
            result.append(y)

    return result

print("Duplicates are ", find_duplicates([1, 1, 2, 2, 5, 1, 5, 6]))
### output ###
# [1, 2, 5]
