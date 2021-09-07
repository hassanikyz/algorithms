def printPascal(s) :

    if s == 0:
      return [1]
    
    if s == 1:
      return [1, 1]
    
    slate = printPascal(s - 1)
    result = []
    result.append(1)
    for i in range(len(slate) - 1):
      result.append(slate[i] + slate[i+1])
    
    result.append(1)
    
    return result

print("Result for row = 5", printPascal(5))
###output###
# [1, 5, 10, 10, 5, 1]
