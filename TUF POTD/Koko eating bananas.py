class Solution:
    def minimumRateToEatBananas(self, nums, h):
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2

            hours = sum((pile + mid - 1) // mid for pile in nums)

            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left