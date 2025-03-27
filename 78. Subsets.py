class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            # Append the current subset to the results
            results.append(path[:])
            # Explore further elements to generate new subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack by removing nums[i] from the current subset
                path.pop()
        
        results = []
        backtrack(0, [])
        return results
