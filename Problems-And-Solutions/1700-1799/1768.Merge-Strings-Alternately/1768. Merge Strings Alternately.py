class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a = len(word1)
        b = len(word2)
        x = range(max(a, b))
        c = ""
        for i in x:
            if i < a:
                c += word1[i]
                if i < b:
                    c += word2[i]
            elif i < b:
                c += word2[i]
        return c