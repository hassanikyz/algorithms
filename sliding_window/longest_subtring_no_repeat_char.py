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
