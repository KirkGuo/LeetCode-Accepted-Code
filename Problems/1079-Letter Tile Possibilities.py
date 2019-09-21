class Solution:
    def __init__(self):
        self.combine_set = set()
        self.ret = 0
    
    def combination(self, marks: List[int], tiles: str):
        tmp_str = ''.join([each for each, idx in zip(tiles, marks) if idx])
        self.combine_set.add(''.join(sorted(tmp_str)))
        cnt = 0
        for idx in range(len(marks)-1):
            if marks[idx] and not marks[idx+1]:
                marks[idx], marks[idx+1] = marks[idx+1], marks[idx]
                marks = [1 for i in range(cnt)] + [0 for i in range(idx-cnt)] + marks[idx:]
                self.combination(marks, tiles)
                return
            else:
                cnt += marks[idx]
        return
    
    def permu_num(self, base: int, select: int) -> int:
        result = 1
        while(select):
            result *= base
            base -= 1
            select -= 1
        return result
    
    def numTilePossibilities(self, tiles: str) -> int:
        for i in range(1, len(tiles)+1):
            marks = [1 for tmp in range(i)] + [0 for tmp in range(len(tiles)-i)]
            self.combination(marks, tiles)
        for each in self.combine_set:
            tmp = self.permu_num(len(each), len(each))
            cnt = collections.Counter(each)
            for key in cnt:
                tmp /= self.permu_num(cnt[key], cnt[key])
            self.ret += int(tmp)
        return self.ret 
