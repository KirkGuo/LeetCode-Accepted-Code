class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ret = []
        for each in intervals:
            if newInterval[0] < each[0]:
                each, newInterval = newInterval, each
            if not ret or ret[-1][1]<each[0]:
                ret.append(each)
            elif ret[-1][1]>=each[1]:
                continue
            else:
                ret[-1][1] = each[1]
        if ret[-1][1]<newInterval[0]:
            ret.append(newInterval)
        elif ret[-1][1]<newInterval[1]:
            ret[-1][1] = newInterval[1]
        return ret
