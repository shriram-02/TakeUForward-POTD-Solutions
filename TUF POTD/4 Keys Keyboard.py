class Solution(object):
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(2, i):
                dp[i] = max(dp[i], dp[i - j] * (j - 1))

        return dp[n]