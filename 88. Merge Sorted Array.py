









class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        # Initialize two pointers for nums1 and nums2 respectively
        p1, p2 = m - 1, n - 1
        # Initialize the pointer for the last index of merged array
        p = m + n - 1

        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, place them in nums1
        # No need to check for nums1 because they are already in place
        nums1[:p2 + 1] = nums2[:p2 + 1]
