class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = list(pattern)
        permu = {}
        letter = ord('a')
        for idx in range(len(pattern)):
            if pattern[idx] not in permu:
                permu[pattern[idx]] = letter
                letter += 1
            pattern[idx] = chr(permu[pattern[idx]])
        
        ret = []
        for each in words:
            tmp = list(each)
            permu = {}
            letter = ord('a')
            for idx in range(len(tmp)):
                if tmp[idx] not in permu:
                    permu[tmp[idx]] = letter
                    letter += 1
                tmp[idx] = chr(permu[tmp[idx]])
            if tmp == pattern:
                ret.append(each)
        return ret  
                
        
