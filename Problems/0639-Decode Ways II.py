class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or '0'==s[0]:
            return 0
        
        m = 10**9 + 7
        
        dp_2 = dp_1 = 0
        dp = 1
        for idx, each in enumerate(s, 1):
            dp_2, dp_1 = dp_1, dp
            if idx==1:
                dp = 1 if each!='*' else 9
                continue
            tstr = s[idx-2:idx]
            if tstr=='**':
                dp = dp_2*15 + dp_1*9
            elif tstr[1]=='*':
                if tstr[0]=='1':
                    dp = dp_2*9 + dp_1*9
                elif tstr[0]=='2':
                    dp = dp_2*6 + dp_1*9
                else:
                    dp = dp_1*9
            elif tstr[0]=='*':
                if tstr[1]=='0':
                    dp = dp_2*2
                elif tstr[1] in '123456':
                    dp = dp_2*2 + dp_1
                else:
                    dp = dp_2 + dp_1
            else:
                if tstr[1]=='0':
                    if tstr[0] not in '12':
                        return 0
                    else:
                        dp = dp_2
                    continue
                if tstr in ['11','12','13','14','15','16','17','18','19','21','22','23','24','25','26']:
                    dp = dp_1 + dp_2
                else:
                    dp = dp_1
            dp = dp % m
        return dp
