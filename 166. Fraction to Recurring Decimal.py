class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')
        num , den = abs(numerator) , abs(denominator)
        res.append(str(num//den))
        remainder = num % den
        if remainder == 0:
            return ''.join(res)
        res.append(".")
        seen = {}
        while remainder != 0:
            if remainder in seen:
                indx = seen[remainder]
                res.insert(indx,"(")
                res.append(")")
                break
            seen[remainder] = len(res)    
            remainder *= 10
            digit = remainder // den
            res.append(str(digit))
            remainder %= den
        return ''.join(res)                    

        
