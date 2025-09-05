class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if (len(word1) != len(word2)):
            return False
        
        map1 = {}
        map2 = {}

        for x in word1:
            map1[x] = map1.get(x, 0) + 1
        
        for x in word2:
            map2[x] = map2.get(x, 0) + 1

        if set(map1.keys()) != set(map2.keys()):
            return False

        if sorted(map1.values()) != sorted(map2.values()):
            return False

        return True
