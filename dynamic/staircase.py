def count_ways(n):
    """
    Staircase can be climbed 1 step, 2 steps or 3 steps at a time

    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair

    Algorithm:
    If you are at last step (top of stairs) and you got there by taking 1 step from the (n - 1) then
    the number of ways you climb the entir stairs is clearly 1 + all num of ways for n -1 stairs.

    Another way to get to top is by taking 2 steps and then adding all num of ways for n - 2 stairs (recursive call)
    Similarly if you took 3 steps to get to top, you can add result from n - 3 recursive call

    Therefore total steps is 
    """

    if n < 0:
        return 0
        
    if n <= 1:
        return 1
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)



def count_ways_memoization(n):

    """
    Same solution as above except intermediate results are now stored in a dictionary so we don't have to calculate them again
    and again.

    
    """

    memo = {}
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    def helper(num):
        if num < 0:
            return 0

        if num <= 1:
            return 1

        if num in memo:
            return memo[num] 
        else:
            memo[num] = helper(num - 1) + helper(num - 2)  + helper(num - 3) 
        
        return memo[num]

    return helper(n)

n = 4
print(f"W/O memoization - Num of ways to climb stairs of size {n} is {count_ways(n)} " )
print(f"With memoization - Num of ways to climb stairs of size {n} is {count_ways_memoization(n)}")


### OUTPUT ###
#W/O memoization - Num of ways to climb stairs of size 4 is 7 
#With memoization - Num of ways to climb stairs of size 4 is 7
