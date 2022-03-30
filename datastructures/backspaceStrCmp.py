  """
  844. Backspace String Compare
  Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

  Note that after backspacing an empty text, the text will continue empty.
  
  """
  
  
  def backspaceCompare( s: str, t: str) -> bool:
        
        #using stack based approach
        #if # is found pop last element from the stack else insert element to the stack
        
        def buildCompare(S):
            res = []
            for c in S:
                if c != '#':
                    res.append(c)
                elif res:
                    res.pop()
            return "".join(res)
            
        return buildCompare(s) == buildCompare(t)
