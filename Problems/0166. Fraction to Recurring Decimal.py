class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = False if numerator*denominator<0 else True
        numerator, denominator = abs(numerator), abs(denominator)
        dec_left = numerator//denominator
        numerator %= denominator
        seen = set()
        dec_right = []
        loop = []
        while numerator:
            while numerator<denominator:
                numerator *= 10
                dec_right.append((0, numerator))
            curr = numerator // denominator
            numerator = (numerator % denominator) * 10
            if (curr, numerator) not in seen:
                seen.add((curr, numerator))
                dec_right.append((curr, numerator))
            else:
                while dec_right[-1]!=(curr, numerator):
                    loop.append(dec_right.pop()[0])
                loop.append(dec_right.pop()[0])
                break
        if dec_right:
            dec_right.pop(0)
        if not dec_right and not loop:
            return '{}'.format('' if flag else '-') + str(dec_left)
        ans = str(dec_left)+'.'+''.join([str(each[0]) for each in dec_right])
        if loop:
            ans += '({})'.format(''.join([str(each) for each in loop[::-1]]))
        return '{}'.format('' if flag else '-') + ans
