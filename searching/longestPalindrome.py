
    def longestPalindrome( s: str) -> str:
        
        
        def isPalindrome(p):
            #string is a plandrome if its same after reversing it
            return p == p[::-1]
        
        
        result = s[0]
        maxlenresult = len(result)
        
        def getLongest(mystr):
            
            j = len(mystr) - 1
            i = 0
            for i in range(len(mystr)):
                while j > i:
                    
                    # starting from the farthest end of the string find a location where the two extreme letters match
                    while (mystr[i] != mystr[j]):
                        j -= 1
                    if j > i and mystr[i] == mystr[j]:
                        possible = mystr[i:j+1]
                        # since we are coming from the farthest end, if this a palindrome it must be the longest
                        if len(possible) > len(result) and isPalindrome(possible):
                            return possible
                    j -= 1
            return mystr[0]
                    
        j = len(s) - 1
        for i in range(len(s)):
            substr = s[i:]

            if len(substr) > len(result):
                longest = getLongest(substr)
                if len(result) < len(longest):
                    result = longest
                
        return result
  
        
        
        
# below solution is correct but not efficient enough
        
#         for i in range(len(s)):
            
#             #treating i as center to expand from and to form a string (potential palindrome) we need to know
#             #how far we are allowed to go on either side of the center before we either hit start/end of the string
#             maxleft = min(i, len(s) - i )
#             centerstart = maxlenresult // 2
#             if centerstart > maxleft:
#                 break
                
#             for j in range(centerstart, maxleft + 1):
                
#                 if j >= maxlenresult//2: 
#                     # expanding to left and right creating a potential palindrome
#                     strcheck = s[i - j: i + j + 1]
#                     if isPalindrome(strcheck):
#                         if len(result) < len(strcheck):
#                             result = strcheck
#                             strcheck = s[i - j: i + j + 1]

#                     # another potential palindrome is even numbered 
#                     # e.g aba and abba are both possible palindrome when we consider center as first b
#                     # thus first checking if we are still within bounds of string
#                     if (i+j+2) < len(s):
#                         strcheck = s[i - j: i + j + 2]
#                         if isPalindrome(strcheck):
#                             if len(result) < len(strcheck):
#                                 result = strcheck
#                 maxlenresult = len(result)
                        
#         return result
    
