"""
Leetcode 746

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""


def minCostClimbingStairs_ButtomUp(cost: List[int]) -> int:

    dp = [0]*(len(cost))

    # Since you can take 1 step or 2 steps to climb these stairs, so let's store (remember) cost of each step against the step that can be taken in an array
    dp[0] = cost[0]
    dp[1] = cost[1]

    # now starting with 3rd step let's build upon minimum cost for each and then at the end look at min of the final two values since there are 
    # two possible steps that can be taken at any given time.
    for i in range(2, len(cost)):
        
        # recurrence equation is essentially cost of stepping on ith stair + min of either getting to 1 step before it or 2 steps before.
        dp[i] = cost[i] + min(dp[i-1], dp[i-2] )

    # Top location has 0 cost of its own (when you step on it). Now getting to top can happen either of two ways, you take 1 step to or 2 steps to get to top. 
    # hence min cost to top is min of either of the two prior values
    return min(dp[-1], dp[-2])

  """
Output 
cost: [1,100,1,1,1,100,1,1,100,1]
state of DP variable close to return 
dp: [1,100,2,3,3,103,4,5,104,6]
i: 9
"""
