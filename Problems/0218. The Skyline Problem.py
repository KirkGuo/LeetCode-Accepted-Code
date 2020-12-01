class Heap:
    
    def __init__(self, init=None):
        self.data = []
        self.index = collections.defaultdict(set)
        if init is not None:
            self.insert(init)
        
    def insert(self, item):
        self.index[item].add(len(self.data))
        self.data.append(item)
        self.__shift_up(len(self.data)-1)
    
    def delete(self, item):
        idx = next(iter(self.index[item]))
        self.__exchange_index(idx, len(self.data)-1)
        self.index[item].remove(len(self.data)-1)
        self.data.pop()
        self.__shift_down(idx)
    
    def peak(self):
        return self.data[0]
    
    def pop(self, item):
        self.__exchange_index(0, len(self.data)-1)
        self.index[self.data[-1]].remove(len(self.data)-1)
        ret = self.data.pop()
        self.__shift_down(0)
        return ret
    
    def __shift_up(self, idx):
        if idx == 0:
            return
        parent = idx - 1 >> 1
        if self.data[parent] < self.data[idx]:
            self.__exchange_index(parent, idx)
            self.__shift_up(parent)
        return
    
    def __shift_down(self, idx):
        left = idx * 2 + 1
        right = left + 1
        if left >= len(self.data):
            return
        if right >= len(self.data):
            if self.data[left] > self.data[idx]:
                self.__exchange_index(left, idx)
            return
        if self.data[idx] >= self.data[left] and self.data[idx] >= self.data[right]:
            return
        if self.data[left] > self.data[right]:
            self.__exchange_index(left, idx)
            self.__shift_down(left)
        else:
            self.__exchange_index(right, idx)
            self.__shift_down(right)
        return  
    
    def __exchange_index(self, x, y):
        if x == y:
            return
        self.index[self.data[x]].remove(x)
        self.index[self.data[y]].remove(y)
        self.data[x], self.data[y] = self.data[y], self.data[x]
        self.index[self.data[x]].add(x)
        self.index[self.data[y]].add(y)
        return
    

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        q = Heap(0)
        points = []
        for p in buildings:
            points.append([p[0], p[2], 0])
            points.append([p[1], p[2], 1])
            
        ret = []
        
        points = sorted(points)
        for p in points:
            prev_max = q.peak()
            if p[2] == 0:
                q.insert(p[1])
                curr_max = q.peak()
                if curr_max > prev_max:
                    ret.append([p[0], p[1]])
            else:
                q.delete(p[1])
                curr_max = q.peak()
                if curr_max < prev_max:
                    ret.append([p[0], curr_max])
        
        ret_new = [ret[0]]
        for i in range(1, len(ret)):
            p = ret[i]
            if p[0] != ret_new[-1][0]:
                ret_new.append(p)
            else:
                ret_new[-1][1] = max(ret_new[-1][1], p[1])
                    
        return ret_new
        
