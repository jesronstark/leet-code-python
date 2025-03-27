class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # Initialize a (m+1) x (n+1) matrix to store the edit distances
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: transforming empty string to a prefix of the other string
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters to transform empty word1 to word2
        
        # Compute the edit distance for each substring
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no additional cost
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Consider all three operations: insert, delete, replace
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Delete
                                       dp[i][j - 1],    # Insert
                                       dp[i - 1][j - 1] # Replace
                                      )
        
        # The edit distance between the two full strings
        return dp[m][n]
