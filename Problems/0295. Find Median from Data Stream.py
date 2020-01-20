class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.integers = [0 for i in range(101)]
        self.extra_left = []
        self.extra_right = []
        self.len = 0

    def addNum(self, num: int) -> None:
        if 0<=num<=100:
            self.integers[num] += 1
        elif num<0:
            self.extra_left.append(num)
            self.extra_left.sort()
        else:
            self.extra_right.append(num)
            self.extra_right.sort()
        self.len += 1
    
    def findIdx(self, idx):
        if len(self.extra_left)>idx:
            return self.extra_left[idx]
        idx -= len(self.extra_left)
        for i, each in enumerate(self.integers):
            idx -=  each
            if idx<0:
                return i
        return self.extra_right[idx]

    def findMedian(self) -> float:
        if self.len%2:
            mid = self.len//2
            return self.findIdx(mid)
        else:
            mid = self.len//2 - 1
            return (self.findIdx(mid) + self.findIdx(mid+1)) / 2
        
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
