class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers, add them, and convert back to binary string
        return bin(int(a, 2) + int(b, 2))[2:]
