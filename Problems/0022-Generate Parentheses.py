class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        if n==1:
            return ['()']
        dp = [set() for i in range(n+1)]
        dp[0].add('')
        dp[1].add('()')
        for step in range(2, n+1):
            print(dp)
            for i in range(step):
                if i==0:
                    dp[step] = dp[step].union(['(' + each + ')' for each in dp[step-1]]) 
                else:
                    dp[step] = dp[step].union([each1+each2 for each1 in dp[i] for each2 in dp[step-i]])
        return list(dp[n])
