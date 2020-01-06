class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.halfQuickSort(nums, 0, len(nums)-1)
        while pos!=k:
            if pos<k:
                pos = self.halfQuickSort(nums, pos, len(nums)-1)
            else:
                pos = self.halfQuickSort(nums, 0, pos-1)
        return nums[pos-1]
    
    def halfQuickSort(self, nums, left, right):
        curr = left
        while left<right:
            while right>left and nums[right]<=nums[curr]:
                right -= 1
            while left<right and nums[left]>=nums[curr]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        if curr!=left:
            nums[curr], nums[left] = nums[left], nums[curr]
        return left+1
