class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while(start<=end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[end]:
                if nums[mid]<target<=nums[end]:
                    start, end = mid+1, end
                else:
                    start, end = start, mid-1
            else:
                if nums[start]<=target<nums[mid]:
                    start, end = start, mid-1
                else:
                    start, end = mid+1, end
        return -1
