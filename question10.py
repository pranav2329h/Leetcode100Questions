#268. Missing Number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit=len(nums)
        actsum=(limit*(limit+1))/2
        currsum=0
        for i in range(len(nums)):
            currsum=currsum+nums[i]
        ans=actsum-currsum
        return ans