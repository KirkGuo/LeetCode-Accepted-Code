class Solution:
    def helper(self, nums, tgt, isMin=True):
        i, j = 0, len(nums)-1
        while i<j:
            m = (i+j)//2 if isMin else (i+j+1)//2
            if isMin:
                if nums[m]>=tgt:
                    j = m
                else:
                    i = m+1
            else:
                if nums[m]>tgt:
                    j = m-1
                else:
                    i = m
        if nums and nums[i]==tgt:
            return i
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.helper(nums, target)
        right = self.helper(nums, target, False)
        return [left, right]
