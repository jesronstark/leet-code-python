class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        # Initialize the heights array with zeros, one more than the number of columns
        heights = [0] * (len(matrix[0]) + 1)
        
        for row in matrix:
            for i in range(len(matrix[0])):
                # Update the heights array: increment height if '1', reset to 0 if '0'
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate the maximum area for the current histogram
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
