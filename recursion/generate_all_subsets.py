def generate_all_subsets(s):

    def helper(slate, s, pos):

        if (pos >= len(s)):
            res.append("".join(slate))
            print("".join(slate))
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
