class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = self.merge(nums1, nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2] + merged[n // 2 - 1]) / 2.0
        else:
            return merged[n // 2]

    def merge(self, arr1, arr2):
        ans = [0] * (len(arr1) + len(arr2))
        p1 = 0
        p2 = 0
        p3 = 0
        while p1 < len(arr1) or p2 < len(arr2):
            val1 = arr1[p1] if p1 < len(arr1) else float('inf')
            val2 = arr2[p2] if p2 < len(arr2) else float('inf')
            if val1 < val2:
                ans[p3] = val1
                p1 += 1
            else:
                ans[p3] = val2
                p2 += 1
            p3 += 1
        return ans
