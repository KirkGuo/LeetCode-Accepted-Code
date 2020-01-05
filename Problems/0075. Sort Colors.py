class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        curr = i
        
        while curr<=j:
            if nums[curr]==0:
                nums[i], nums[curr] = nums[curr], nums[i]
                i += 1
                curr += 1
            elif nums[curr]==2:
                nums[j], nums[curr] = nums[curr], nums[j]
                j -= 1
            else:
                curr += 1
                
