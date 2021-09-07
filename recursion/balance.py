

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
