class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            # If the combination is of the desired length, add it to the results
            if len(path) == k:
                results.append(path[:])
                return
            # Iterate over the range from the current number to n
            for i in range(start, n + 1):
                # Include the current number in the combination
                path.append(i)
                # Move on to the next number
                backtrack(i + 1, path)
                # Backtrack by removing the last number added
                path.pop()
        
        results = []
        backtrack(1, [])
        return results
