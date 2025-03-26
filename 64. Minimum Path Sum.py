class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        
        # Initialize the first column
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]
        
        # Fill in the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[m - 1][n - 1]
