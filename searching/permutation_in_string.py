
"""
https://leetcode.com/problems/permutation-in-string/
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""
def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    lens1 = len(s1)
    lens2 = len(s2)

    sorteds1 = sorted(s1)
    for i in range(lens2 - lens1 + 1):
        sub_str2 = s2[i:i+lens1]
        if sorted(sub_str2) == sorteds1:
            return True

    return False

  
  """
  input 
  s1 = "ab"
  s2 = "eidbaooo"
  
  Output: True
  """
