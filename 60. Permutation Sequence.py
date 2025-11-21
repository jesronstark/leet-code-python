











class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        # Create a list of numbers to get indices
        numbers = list(range(1, n + 1))
        # Adjust k to be zero-indexed
        k -= 1
        # Initialize the result
        result = []

        # Generate the permutation
        for i in range(n, 0, -1):
            # Determine the index of the current digit
            index, k = divmod(k, factorial(i - 1))
            result.append(str(numbers[index]))
            # Remove used number
            numbers.pop(index)

        return ''.join(result)
