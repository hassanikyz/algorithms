

"""
Challenge:
Given an array that contains opening and closing brackets, check whether or not the brackets are balanced in the array.

Example of balanced
()

(())

(())()

((()))((()))

Example of unbalanced

(

)()(

((()()()()

((())))((((()


RECURSIVE APPROACH
There are two pointers startIndex and currentIndex.
startIndex traverses the entire list
currentIndex increases when '(' is found and decreases when ')' is found. 

"""
def balanced(lst, startIndex = 0, currentIndex = 0) :

  if startIndex == len(lst):
    return currentIndex == 0

  if currentIndex < 0:
    return False

  if lst[startIndex] == "(":
    return balanced(lst, startIndex+1, currentIndex+1)
  
  
  if lst[startIndex] == ")":
    return balanced(lst, startIndex+1, currentIndex-1)
  
  
  
print(balanced(['(', '(', ')', ')', '(', ')'])	)
## True	is expected
print(balanced(['(', ')', '(', ')']))
## True	is expected
print(balanced([')', '('])  )
## False is expected

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
