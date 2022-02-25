"""
https://leetcode.com/problems/max-area-of-island/
Problem # 695

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        covered = {}
                
        m = len(grid)
        n = len(grid[0])
        
        def makekey(i, j):
            return str(i) + '-' + str(j)
        
        def dfs_area(r, c, grid):
            new_area = 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                key = makekey(r,c)
                covered[key] = 1
                new_area += 1
                key = makekey(r - 1, c)
                if r - 1 >= 0 and key not in covered:
                    new_area += dfs_area(r-1, c, grid)
                key = makekey(r, c - 1)
                if c - 1 >= 0 and key not in covered:
                    new_area += dfs_area(r, c-1, grid)
                key =makekey(r+1, c)
                if r+1 < m and key not in covered:
                    new_area += dfs_area(r+1, c, grid)
                key = makekey(r , c + 1)
                if c+1 < n and key not in covered:
                    new_area += dfs_area(r, c+1, grid)
                    
            
            return new_area
            
            
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    #new_area = 1
                    new_area = dfs_area(i,j , grid)
                    if new_area > max_area:
                        max_area = new_area
                        
                        
        return max_area
