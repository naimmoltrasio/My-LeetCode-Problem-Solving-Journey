class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumLeft = []
        sumRight = [0] * (n+1) 
        

        for i in range(n):
            if i == 0:
                sumLeft.append(nums[i])
            else:
                result = sumLeft[i-1] + nums[i]
                sumLeft.append(result)

        for i in range(n-1, -1, -1): 
            sumRight[i] = sumRight[i+1] + nums[i]
        
        for i in range(n):
            if sumRight[i] == sumLeft[i]:
                return i

        return -1