class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda item:item[0])
        merged = []
        for each in intervals:
            if not merged or each[0]>merged[-1][1]:
                merged.append(each)
            elif each[1]<=merged[-1][1]:
                continue
            else:
                merged[-1][1] = each[1]
        return merged
                
