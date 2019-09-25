class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        interval = [left, right]
        inserted = False
        for idx in range(len(self.ranges)):
            if self.ranges[idx][0] > left:
                self.ranges[idx], interval = interval, self.ranges[idx]
            if self.ranges[idx][1] >= interval[1]:
                inserted = True
                break
            if self.ranges[idx][1] <= interval[0]:
                continue
            self.ranges[idx][1] = interval[1]
            inserted = True
            break
        if not inserted:
            self.ranges.append(interval)
        new_interval = []
        for idx in range(len(self.ranges)-1):
            if self.ranges[idx][1]<self.ranges[idx+1][0]:
                new_interval.append(self.ranges[idx])
            else:
                self.ranges[idx+1][0] = self.ranges[idx][0]
                self.ranges[idx+1][1] = max(self.ranges[idx+1][1], self.ranges[idx][1])
        new_interval.append(self.ranges[-1])
        self.ranges = new_interval
        return

    def queryRange(self, left: int, right: int) -> bool:
        for each in self.ranges:
            if each[1] < left:
                continue
            if each[0]<=left and each[1]>=right:
                return True
            if each[1]<=left:
                return False
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_interval = []
        for each in self.ranges:
            if each[1]<=left or each[0]>=right:
                new_interval.append(each)
            elif each[0]<left and each[1]<=right:
                new_interval.append([each[0], left])
            elif each[0]>=left and each[1]>right:
                new_interval.append([right, each[1]])
            elif each[0]<left and each[1]>right:
                new_interval.append([each[0], left])
                new_interval.append([right, each[1]])
        self.ranges = new_interval
        return
            


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
