
class Solution:
    def anagramMappings(self, nums1, nums2):
        mp = {}

        for i, num in enumerate(nums2):
            mp.setdefault(num, []).append(i)

        ans = []

        for num in nums1:
            ans.append(mp[num].pop())

        return ans
