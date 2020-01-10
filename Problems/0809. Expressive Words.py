class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def group_ch(S):
            s = []
            ch = '#'
            curr = 1
            for each in S:
                if each!=ch:
                    s.append([ch, curr])
                    curr = 1
                    ch = each
                else:
                    curr += 1
            s.append([ch, curr])
            return s[1:]
        
        target = group_ch(S)
        ans = 0
        for each in words:
            curr = group_ch(each)
            if len(curr)!=len(target):
                continue
            match = True
            for i in range(len(target)):
                if curr[i][0]!=target[i][0]:
                    match = False
                    break
                if target[i][1]<3 and target[i][1]!=curr[i][1]:
                    match = False
                    break
                if target[i][1]<curr[i][1]:
                    match = False
                    break
            if match:
                ans += 1
        return ans
        
