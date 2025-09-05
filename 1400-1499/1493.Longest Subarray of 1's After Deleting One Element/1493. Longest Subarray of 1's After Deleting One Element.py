class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        earlyzero, leng = 0, 0
        left = 0
        erased = False
        n = len(nums)

        s = set(nums)
        
        if(len(s) == 1 and nums[0] == 1):
            return n - 1
        else:
            for i in range(n):
                if nums[i] == 0:
                    if erased == False:
                        erased = True
                        earlyzero = i
                    else:
                        left =  earlyzero + 1
                        earlyzero = i
                
                t = i - left

                if (t) > leng:
                    leng = t

            return leng