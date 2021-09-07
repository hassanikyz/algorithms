def printPascal(s) :

    if s == 0:
      return [1]
    
    if s == 1:
      return [1, 1]
    
    ## Using recursion to get the result of previous number and using that to build result for this number ##
    ## Pascal Triangle is essentially 
    ##                        1
    ##                      1   1
    ##                    1   2    1
    ##                  1   3    3    1
    ##                1   4    6    4    1
    ##              1   5   10   10    5    1
    
    slate = printPascal(s - 1)
    result = []
    result.append(1)
    for i in range(len(slate) - 1):
      result.append(slate[i] + slate[i+1])
    
    result.append(1)
    
    return result

print("Result for row = 5: ", printPascal(5))
###output###
# Result for row = 5: [1, 5, 10, 10, 5, 1]
