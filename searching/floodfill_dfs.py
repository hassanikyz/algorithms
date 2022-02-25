"""
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        
        color = image[sr][sc]
        
        def dfs(image, sr, sc, color, newColor):
            
            if image[sr][sc] == color:
                image[sr][sc] = newColor
                if sr-1>=0:
                    dfs(image, sr-1, sc, color, newColor)
                if sc-1>=0:
                    dfs(image, sr, sc-1, color, newColor)
                if sr+1 < m:
                    dfs(image, sr+1, sc, color, newColor)
                if sc+1 < n:
                    dfs(image, sr, sc+1, color, newColor)
                
        if color != newColor:
            dfs(image, sr, sc, color, newColor)     
            
        return image
                    
                
