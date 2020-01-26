class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, val: int) -> None:
        if not self.data:
            self.data.append([val, val])
            return
        bisect.insort(self.data, [val, val])
        tmp = []
        for each in self.data:
            if not tmp:
                tmp.append(each)
            else:
                prev = tmp[-1]
                if each[0]>prev[1]+1:
                    tmp.append(each)
                elif each[0]<=prev[1]+1:
                    tmp[-1][1] = max(each[1], tmp[-1][1])
        self.data = tmp
        return
            

    def getIntervals(self) -> List[List[int]]:
        return self.data


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
