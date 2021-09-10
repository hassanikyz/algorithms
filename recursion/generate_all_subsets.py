def generate_all_subsets(s):

    def helper(slate, s, pos):

        """
        Generating all subsets mean we explore all possible combinations. Going through the input we have two options when creating a set
        1. Include the element
        2. Not include the element
        
        E.g "abc"
        We don't include anything we get empty set
        ""
        We include just the first element
        "a"
        Using these two sets as base we can now repeat the same process with next element in the input
        "" + "b" => "b"
        and
        "a" + "b"  => "ab" 
        Similarly for the 3rd input 'c' we have previous 4 sets to use as base and create 4 more sets by adding 3 to each
        
        Recursive approach works here. 
        Base case is to stop when we have gone through all elements. This is done by using a helper function with input as pointer to a position in the string
        We keep a temporary list as 'slate' where we collect subsets and at the end join the elements into a string and put in final result.
        
        
        """
        
        if (pos >= len(s)):
            res.append("".join(slate))
        else:
    
            if len(slate) == 0 or s[pos] not in slate:
                slate.append("")
                helper(slate, s, pos+1)
                slate.pop()
  
            slate.append(s[pos])
            helper(slate, s, pos+1)
            slate.pop()

    res = []
    slate = []
    helper(slate, s, 0)
    return res   

inp = "abcd"
print(f"All subsets for {inp} are\n {generate_all_subsets(inp)}")
