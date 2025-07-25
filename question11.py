#27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ptr=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[ptr]=nums[i]
                ptr+=1
        return ptr
        