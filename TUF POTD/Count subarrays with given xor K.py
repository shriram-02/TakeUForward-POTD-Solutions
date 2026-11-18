class Solution:
    def subarraysWithXorK(self, nums, k):
        freq = {0: 1}
        xor = 0
        count = 0

        for num in nums:
            xor ^= num
            count += freq.get(xor ^ k, 0)
            freq[xor] = freq.get(xor, 0) + 1

        return count