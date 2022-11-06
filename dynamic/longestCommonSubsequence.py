"""
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Example 1:

Input:
x = 6, y = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
"""

def lcs(x,y,s1,s2):
    
    # code here
    # Explanation of the alogrithm
    
    # Imagine a 2D array where num of rows correspond to length of one string and num of columns to second string
    # this 2D grid has letters on columns and rows 
    
    dp = [[0 for i in range(y + 1)] for j in range(x + 1)]
    
    
    for i in range(x - 1, -1,  -1):
        for j in range(y - 1, -1,  -1):
            
            #traveling up the 2D, if last letter of both strings same then we know at least 1 subsequence match
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                
    return dp[0][0]
