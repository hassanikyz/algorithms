"""

https://leetcode.com/problems/longest-substring-without-repeating-character
input string = "abcbccbb"
Answer = 3

"""

    def lengthOfLongestSubstring(s: str) -> int:
        
        ## sliding window technique, keep two pointers front one expands and behind one contracts
        behind = 0
        front = 0
        max_res = 0
        
        charmap = {}
        
        while front < (len(s)):
            
            if s[front] not in charmap:
                charmap[s[front]] = 1
                front += 1
                max_res = max(max_res, len(charmap))
            else:
                del charmap[s[behind]]
                behind += 1
        
        
        return max_res

    
    
    """ 
    Solution # 2 : Easer to understand
    """
    
     def lengthOfLongestSubstring(s: str) -> int:
        
        result = ""
        curr_max = ""
        if len(s) == 0:
            return 0
        
        for c in s:    
            
            # keep taking one character at a time and keep appending to curr_max if no repeated character is found
            # otherwise remove all characters upto and including the first repetition seen
            if c in curr_max:
                # if character is found inside the curr_max string, find its index and remove all characters upto and including the repeated character
                i = curr_max.index(c, 0, len(curr_max))
                curr_max = curr_max[i+1:] + c
                # keep track of curr_max's length
            else:
                # keep adding 
                curr_max += c
            
            # final result is max of curr_max every is. 
            if len(result) < len(curr_max):
                result = curr_max


        return result
