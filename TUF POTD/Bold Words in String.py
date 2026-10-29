class Solution(object):
    def boldWords(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: str
        """
        bold = [False] * len(s)

        for word in words:
            start = 0
            while True:
                i = s.find(word, start)
                if i == -1:
                    break
                for j in range(i, i + len(word)):
                    bold[j] = True
                start = i + 1

        result = []
        i = 0

        while i < len(s):
            if not bold[i]:
                result.append(s[i])
                i += 1
            else:
                result.append("<b>")
                while i < len(s) and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")

        return "".join(result)