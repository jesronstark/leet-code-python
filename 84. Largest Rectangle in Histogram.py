class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Initialize a stack to store indices of histogram bars
        stack = []
        max_area = 0
        index = 0

        # Iterate through all bars of the histogram
        while index < len(heights):
            # If this bar is higher than the bar at stack top, push it to the stack
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top
                top_of_stack = stack.pop()
                # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar 'h'
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                # Update max_area, if needed
                max_area = max(max_area, area)

        # Now, pop the remaining bars from the stack and calculate area with each popped bar
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

        return max_area
