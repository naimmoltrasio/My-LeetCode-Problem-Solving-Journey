class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxc = 0
        count = 0
        vowels = set(["a", "e", "i", "o", "u"])
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxc = count  
        if count == k:
            return k

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count == k:
                return k
            elif count > maxc:
                maxc = count

        return maxc