class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n,rem=divmod(abs(numerator),abs(denominator))
        sn='-' if numerator * denominator<0 else ''
        frac=[sn+str(n)]
        if rem==0:
            return ''.join(frac)
        frac.append('.')
        mydict={}
        while rem!=0:
            if rem in mydict:
                frac.insert(mydict[rem],'(')
                frac.append(')')
                break
            mydict[rem]=len(frac)
            n,rem=divmod(rem*10,abs(denominator))
            frac.append(str(n))
        return ''.join(frac)