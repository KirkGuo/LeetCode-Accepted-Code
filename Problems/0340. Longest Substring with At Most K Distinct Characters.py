class Heap:
    
    def __init__(self):
        
        self.heap = []
        self.char2heapIdx = {}
        
    def insert(self, char, idx):
        
        self.char2heapIdx[char] = len(self.heap)
        self.heap.append([idx, char])
        
    def updata_idx(self, char, idx):
        heapIdx = self.char2heapIdx[char]
        self.heap[heapIdx][0] = idx
        self.shift_down(heapIdx)
        
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        idx, char = self.heap[0]
        self.char2heapIdx[self.heap[0][1]] = 0
        self.char2heapIdx.pop(self.heap[-1][1])
        ret = self.heap.pop()
        self.shift_down(0)
        
        return ret
    
    def shift_down(self, idx):
        left = (idx << 1) + 1
        right = (idx << 1) + 2
        if left >= len(self.heap):
            return
        if right >= len(self.heap):
            if self.heap[left] < self.heap[idx]:
                self.exchange(idx, left)           
            return
        
        if self.heap[idx] <= self.heap[left] and self.heap[idx] <= self.heap[right]:
            return
        
        if self.heap[left] < self.heap[right]:
            self.exchange(idx, left)
            self.shift_down(left)
        else:
            self.exchange(idx, right)
            self.shift_down(right)
        return
    
    def exchange(self, x, y):
        char, char_ = self.heap[x][1], self.heap[y][1]
        self.char2heapIdx[char], self.char2heapIdx[char_] = y, x
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
        return

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        best = 0
        
        if not s or not k:
            return best
        
        startIdx = 0
        
        preIdx = Heap()
        
        inStr = set()
        
        for i, each in enumerate(s):
            # print(preIdx.heap, preIdx.char2heapIdx, startIdx, i, each)
            if each in inStr:
                preIdx.updata_idx(each, i)
            else:
                inStr.add(each)
                preIdx.insert(each, i)
                if len(inStr) > k:
                    idx, char = preIdx.pop()
                    inStr.remove(char)
                    best = max(best, i - startIdx)
                    startIdx = idx + 1
        best = max(best, i - startIdx + 1)
        return best
