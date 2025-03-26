class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trim any trailing spaces from the string
        s = s.rstrip()
        # Initialize a counter for the length of the last word
        length = 0
        # Iterate backwards over the string
        for char in reversed(s):
            if char == ' ':
                # When the first space is encountered after a word, break
                break
            length += 1
        return length
