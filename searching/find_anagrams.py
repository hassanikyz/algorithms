def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """

    if len(lst) < 2:
        return lst
    
    mydict = {}
    for i in range(len(lst)):
        key = "".join(sorted(lst[i]))
        if key in mydict:
            mydict[key].append(i)
        else:
            mydict[key] = [i]

    result = []
    for key in mydict:
        vals = []
        for x in mydict[key]:
            vals.append(lst[x])        
        result.append(vals)

    return result

input = [
    'tom marvolo riddle ',
    'abc',
    'def',
    'cab',
    'fed',
    'brag',
    'clint eastwood ',
    'i am lord voldemort',
    'elvis',
    'grab',
    'old west action',
    'lives'
  ]
print("Pairs of Anagrams are \n: ", anagrams(input))
