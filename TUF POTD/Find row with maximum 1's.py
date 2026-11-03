class Solution:
    def rowWithMax1s(self, mat):
        max_ones = 0
        ans = -1

        for i, row in enumerate(mat):
            count = sum(row)
            if count > max_ones:
                max_ones = count
                ans = i

        return ans