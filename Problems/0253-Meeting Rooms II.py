class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ans = 0
        starts = sorted([item[0] for item in intervals])
        ends = sorted([item[1] for item in intervals])
        pend = 0
        for i in range(len(starts)):
            if starts[i]<ends[pend]:
                ans += 1
            else:
                pend += 1
        
        return ans
