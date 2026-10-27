class Solution:
    def anagramStrings(self, s, t):
        return sorted(s) == sorted(t)