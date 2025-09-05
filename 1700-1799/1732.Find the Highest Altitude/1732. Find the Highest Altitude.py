class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = []
        alt.append(0)
        highest = 0
        for i in range(1, len(gain)+1):
            x = gain[i-1] + alt[i-1]
            alt.append(x)
       
        highest = max(alt)
        return highest