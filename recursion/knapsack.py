
"""
Problem Statement#
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such 
that their cumulative weight is not more than a given number ‘C’. Write a function that returns the maximum profit. 
Each item can only be selected once, which means either we put an item in the knapsack or skip it.

Solution Approach
We are going to try different combination by including an item in our set or not including in our set. For example if we select item #1, 
we would calculate the weight and profit and another combination when we don't include it.


For example various combinations if 3 items are
[nothing] => 0 profit
item 1 only => profit from item 1 only
item 1 + item2 => profit from both items 1 and 2
item 1 + item3  (skipping 2) => profit from both items 1 and 3
item 1 + item 2 + item 3 => profit from all three items 1,2,3
item 2 => profit from item 2 only
item 2 + item 3 => profit from both items 2 and 3
item 3 => profit from item 3 only
"""
def solve_knapsack(profits, weights, capacity):

  def knapsack_recursive(profits, weights, capacity, index):

    # basecase if capacity left is 0 or negative 
    # or if index exceeds the items given 
    # that means we didn't find any solution
    if capacity <= 0 or index >= len(weights):
      return 0

    profit1 = 0
    if weights[index] <= capacity:   # means we have space for accomodating more items
      
      # profit from current item + profit from items with remaining capacity (using recursion)
      profit1 = profits[index] + knapsack_recursive(profits, weights, capacity - weights[index], index+1) 

    # skipping current items and calculating profit from all the remaining ones. With two options we will get the max of the two at the end
    profit2 = knapsack_recursive(profits, weights, capacity, index+1)
    
      
    return max(profit1, profit2)


  return knapsack_recursive(profits, weights, capacity, 0)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
