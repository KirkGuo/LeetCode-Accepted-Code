class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        def helper(j, i=0):
            while i<j:
                p, q = i+1, j-1
                while p<q:
                    curr = nums[i] + nums[j] + nums[p] + nums[q]
                    if curr==target:
                        ans.add((nums[i], nums[p], nums[q], nums[j]))
                        p += 1
                    elif curr > target:
                        q -= 1
                    else:
                        p += 1
                i += 1
        for j in range(n-1, -1, -1):
            helper(j)
        return list(ans)
            
