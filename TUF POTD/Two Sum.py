
class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in mp:
                return [mp[complement], i]

            mp[num] = i
