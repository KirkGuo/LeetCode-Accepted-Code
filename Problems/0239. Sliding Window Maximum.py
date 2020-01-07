class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k==1:
            return nums
        
        def cleanQueue(deq, i):
            if deq and deq[0]==i-k:
                deq.pop(0)
            while deq and nums[deq[-1]]<nums[i]:
                deq.pop()
        
        ans = [nums[0]]
        deq = []
        for i in range(k):
            ans[0] = max(ans[0], nums[i])
            cleanQueue(deq, i)
            deq.append(i)
        
        for i in range(k, len(nums)):
            cleanQueue(deq, i)
            deq.append(i)
            ans.append(nums[deq[0]])
        
        return ans
