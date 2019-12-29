class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks)>1:
            curr = 0
            curr += heapq.heappop(sticks)
            curr += heapq.heappop(sticks)
            ans += curr
            heapq.heappush(sticks, curr)
        return ans
        
