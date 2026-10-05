class Solution:
    def minimumCost(self, target: str, words: list, costs: list) -> int:
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            for word, cost in zip(words, costs):
                if target.startswith(word, i):
                    j = i + len(word)
                    dp[j] = min(dp[j], dp[i] + cost)

        return -1 if dp[n] == float('inf') else dp[n]