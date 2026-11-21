class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        max_len = 0
        mp = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in mp:
                max_len = max(max_len, i - mp[prefix_sum - k])

            if prefix_sum not in mp:
                mp[prefix_sum] = i

        return max_len