
def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    ### find the two largest numbers by value since their product will be the largest
    if len(lst) <= 1:
        return 0, 0

    mx_val = lst[0]
    last_mx_val = mx_val
    for i in lst:
        if i >= mx_val:
            last_mx_val = mx_val
            mx_val = i

    return [mx_val, last_mx_val]

print("Pair producing max product: ", find_max_prod([1, 2, 3, 4, 5, 6, 7, 8]))
#### output ###
###  [8, 7]
