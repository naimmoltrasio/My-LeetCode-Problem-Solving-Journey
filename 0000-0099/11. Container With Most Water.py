class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) - 1
        cpt = 0
        x = 0
        i = 0
        
        while i != n:
            left = height[i]
            right = height[n]
            x = min(left, right) * (n-i)
            if x > cpt:
                cpt = x
            else:
                if left < right:
                    i = i + 1
                else:
                    n = n - 1

        return cpt  