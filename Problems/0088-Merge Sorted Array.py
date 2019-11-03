class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m
        for each in nums2:
            nums1[l] = each
            l += 1
        nums1.sort()
