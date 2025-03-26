class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define the boundaries of the spiral
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1  # Start filling with 1
        
        while num <= n * n:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary downward
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary leftward
            
            # Traverse from right to left along the bottom boundary
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move the bottom boundary upward
            
            # Traverse from bottom to top along the left boundary
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1  # Move the left boundary rightward
        
        return matrix
