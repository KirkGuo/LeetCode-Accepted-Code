class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        ans = right
        while left<right:
            mid = (left+right)>>1
            groups = 1
            curr = 0
            for each in nums:
                if curr+each>mid:
                    groups += 1
                    curr = each
                else:
                    curr += each
            if groups<=m:
                right = mid
            else:
                left = max(left+1, mid)
        ans = left
        return ans
                    
