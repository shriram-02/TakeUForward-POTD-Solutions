class Solution:
    def isDivisibleBy9(self, s: str) -> bool:
        return sum(int(ch) for ch in s) % 9 == 0