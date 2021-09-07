
"""
ITERATIVE Approach:
keep a variable called balance and increment it as you find '(' and decrement it as you find '('. At any given time if balance is negative it means unbalanced.
if balance = 0 after traversing entire list then all good. If it is negative at the end, then it is unbalanced.

"""

def balanced_iter(lst, startIndex = 0, currentIndex = 0) :

  balance = 0

  while balance >= 0 and currentIndex < len(lst):
    while   currentIndex < len(lst) and lst[currentIndex] == '(' :
      balance += 1 
      currentIndex += 1
    while  currentIndex < len(lst) and lst[currentIndex] == ')' :
      balance -= 1
      currentIndex += 1

    if balance < 0:
      return False

  if balance < 0:
      return False
  return True

print("Balanced is ", balanced_iter([')', ')', '(', '(',  '(', ')']))
