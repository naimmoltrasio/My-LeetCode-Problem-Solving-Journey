class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums) - 1 
        i = 0
        result = 0

        while i < n:
            s = nums[i] + nums[n]
            if s == k:
                result += 1
                i += 1
                n -= 1
            elif s > k:
                n -= 1
            else:
                i += 1

        return result