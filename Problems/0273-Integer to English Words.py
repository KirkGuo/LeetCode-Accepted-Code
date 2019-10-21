class Solution:
    def numberToWords(self, num: int) -> str:
        def describe_gourp(num):
            descrip = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
            descrip_tens = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen',
                           17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 10:'Ten'}
            descrip_dec = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty',    
                           9:'Ninety'}
            ans = ''
            
            if not num:
                return ''
            if num // 100:
                ans += descrip[num//100] + ' Hundred'
            num %= 100
            if num in descrip_tens:
                ans += ' ' + descrip_tens[num]
            else:
                if num//10:
                    ans += ' ' + descrip_dec[num//10]
                if num%10:
                    ans += ' ' + descrip[num%10]
            return ans
                
        groups = []
        while num:
            groups.append(num%1000)
            num //= 1000
        descriptor = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        ans = ''
        print(groups)
        for idx, each in enumerate(groups):
            descrip = describe_gourp(each)
            if descrip and idx:
                ans = descrip + ' ' + descriptor[idx] + ' ' + ans
            elif descrip:
                ans = descrip
        return ' '.join(ans.split()) if ans else 'Zero'
