#1464. Maximum Product of Two Elements in an Array
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smax=-1
        max=-1
        for i in range(len(nums)):
            if max< nums[i]:
                smax=max
                max=nums[i]
            elif smax < nums[i]:
                smax=nums[i]
        ans=(max-1)*(smax-1)
        return ans