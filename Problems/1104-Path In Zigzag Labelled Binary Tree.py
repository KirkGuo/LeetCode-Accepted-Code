class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def num2idx(num: int) -> List[int]:
            if num<1:
                return -1, -1
            i = 0
            while(num>=pow(2,i)):
                i += 1
            i -= 1
            j = num-pow(2,i) if i%2==0 else pow(2,i+1)-1-num
            return i, j
        def idx2num(i: int, j: int) -> int:
            return pow(2,i)+j if i%2==0 else pow(2,i+1)-1-j
        
        ret = []
        ret.append(label)
        idx_last = num2idx(label)
        while idx_last != (0,0):
            idx_last = idx_last[0]-1, idx_last[1]//2
            ret.append(idx2num(idx_last[0], idx_last[1]))
        return  ret[::-1]
