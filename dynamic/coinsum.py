#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'coinSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY coins
#  2. INTEGER total
#
"""
 Create combinations using coins provided. 
              5 (index 0)
      (-1)  /   \  (i++)
           /      \
 (i=0)    4         5  (i=1)
            
            
            
"""
from functools import lru_cache


def coinSum(coins, total):

    length = len(coins)
    
    
    @lru_cache(None)
    def helper(target, index):
        
        if target == 0:
            return 1
        if target < 0:
            return 0
        elif index >= length:
            return 0
        
        left = helper(target - coins[index], index)
        right = helper(target, index+1)

        return left + right

    return helper(total, 0)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(input().strip())

    coins = []

    for _ in range(coins_count):
        coins_item = int(input().strip())
        coins.append(coins_item)

    total = int(input().strip())

    result = coinSum(coins, total)

    fptr.write(str(result) + '\n')

    fptr.close()
