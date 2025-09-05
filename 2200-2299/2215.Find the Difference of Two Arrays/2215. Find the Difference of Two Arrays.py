class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        unique1 = list(nums1 - nums2)
        unique2 = list(nums2 - nums1)

        return list([unique1, unique2])
