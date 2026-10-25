class Solution:
    def count_quadruples(self, s1, s2):
        first = {}
        last = {}

        for i, ch in enumerate(s1):
            if ch not in first:
                first[ch] = i

        for i, ch in enumerate(s2):
            last[ch] = i

        min_diff = float('inf')
        count = 0

        for ch in first:
            if ch in last:
                diff = first[ch] - last[ch]

                if diff < min_diff:
                    min_diff = diff
                    count = 1
                elif diff == min_diff:
                    count += 1

        return count