class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)-1, -1, -1):
            if idx==0:
                nums.sort()
                return
            if nums[idx] > nums[idx-1]:
                break
        j = len(nums)-1
        while j and nums[j]<=nums[idx-1]:
            j -= 1
        nums[idx-1], nums[j] = nums[j], nums[idx-1]
        i = idx
        j = len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
