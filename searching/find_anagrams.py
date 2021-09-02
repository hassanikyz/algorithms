def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """

    if len(lst) < 2:
        return lst
    
    """
    Main idea is anagrams can be found by sorting strings first. Two strings are anagrams if after sort they are equal to each other. 
    Therefore, we iterate thorugh the list and sort each string found in the list. Sorted string act as a key to a dictionary entry. 
    Values against the key are actually a list of indices which point back to original list. 
    
    Once such a dictionary is generated, we iterate through the dictionary and generate a list which carries pairs of anagrams found in original list.
    """
    
    mydict = {}
    for i in range(len(lst)):
        # sorted creates a list of characters which then needs to be joined to recreate the string
        key = "".join(sorted(lst[i]))
        if key in mydict:
            mydict[key].append(i)
        else:
            # value is a list of indices
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

""" 
### output ####
Pairs of Anagrams are 
: [['tom marvolo riddle ', 'i am lord voldemort'], ['abc', 'cab'], ['def', 'fed'], ['brag', 'grab'], ['clint eastwood ', 'old west action'], ['elvis', 'lives']]
"""
