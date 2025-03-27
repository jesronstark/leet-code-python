class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the slow-runner pointer
        i = 0

        # Iterate through the array with the fast-runner pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                # Move the slow-runner pointer forward
                i += 1
                # Update the value at the slow-runner pointer
                nums[i] = nums[j]

        # The length of the array without duplicates is i + 1
        return i + 1
