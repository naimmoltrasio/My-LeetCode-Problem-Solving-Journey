class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = []
        right = [0] * n   
        res = [0] * n

        for i in range(n):
            if i == 0:
                left.append(1) 
            else:
                x = left[i-1] * nums[i-1]
                left.append(x)

        for i in reversed(range(n)):
            if i == n-1:
                right[i] = 1 
            else:
                right[i] = right[i+1] * nums[i+1]

        for i in range(n):
            res[i] = left[i] * right[i]

        return res

