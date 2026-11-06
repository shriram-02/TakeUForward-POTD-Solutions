class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        n = len(word)
        
        def backtrack(i, cur, count):
            if i == n:
                res.append(cur + str(count) if count > 0 else cur)
                return
            
            # Option 1: Abbreviate current character
            backtrack(i + 1, cur, count + 1)
            
            # Option 2: Keep current character
            new_cur = cur + (str(count) if count > 0 else "") + word[i]
            backtrack(i + 1, new_cur, 0)
            
        backtrack(0, "", 0)
        return res